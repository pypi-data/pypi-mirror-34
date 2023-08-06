import hyperopt
import csv
import json
from pprint import pprint
import datetime
import time
import numpy.random
import threading
import queue
import random
import concurrent.futures
import functools
import atexit
from hypermax.execution import Execution
from hypermax.results_analyzer import ResultsAnalyzer

from hypermax.configuration import Configuration


class Optimizer:
    resultInformationKeys = [
        'trial',
        'status',
        'loss',
        'time',
        'log',
        'error'
    ]

    def __init__(self, configuration):
        self.config = Configuration(configuration)

        self.space = self.config.createHyperparameterSpace()

        self.threadExecutor = concurrent.futures.ThreadPoolExecutor()

        self.resultsAnalyzer = ResultsAnalyzer(configuration)

        self.results = []

        self.best = None
        self.bestLoss = None

        self.thread = threading.Thread(target=lambda: self.optimizationThread(), daemon=True)

        self.totalTrials = 1000
        self.trialsSinceDetailedResults = 0
        self.resultsFuture = None

    def __del__(self):
        self.threadExecutor.shutdown(wait=True)

    def completed(self):
        return len(self.results)

    def sampleNext(self):
        rstate = numpy.random.RandomState(seed=int(random.randint(1, 2 ** 32 - 1)))
        params = {}

        def sample(parameters):
            nonlocal params
            params = parameters
            return {"loss": 0, 'status': 'ok'}

        hyperopt.fmin(fn=sample,
                      space=self.space,
                      algo=functools.partial(hyperopt.tpe.suggest, n_EI_candidates=24, gamma=0.25),
                      max_evals=1,
                      trials=self.convertResultsToTrials(self.results),
                      rstate=rstate)

        return params

    def runOptimizationRound(self):
        jobs = self.config.data['function'].get('parallel', 4)
        samples = [self.sampleNext() for job in range(jobs)]

        def testSample(params, trial):
            start = datetime.datetime.now()
            execution = Execution(self.config.data['function'], parameters=params)
            modelResult = execution.run()
            end = datetime.datetime.now()

            result = {}
            result['trial'] = trial

            if 'loss' in modelResult:
                result['loss'] = modelResult['loss']
            elif 'accuracy' in modelResult:
                result['loss'] = modelResult['accuracy']

            if 'status' in modelResult:
                result['status'] = modelResult['status']
            else:
                result['status'] = 'ok'

            if 'log' in modelResult:
                result['log'] = modelResult['log']
            else:
                result['log'] = ''

            if 'error' in modelResult:
                result['error'] = modelResult['error']
            else:
                result['error'] = ''

            if 'time' in modelResult:
                result['time'] = modelResult['time']
            else:
                result['time'] = (end-start).total_seconds()

            def recurse(key, value, root):
                result_key = root + "." + key
                if isinstance(value, str):
                    result[result_key[1:]] = value
                elif isinstance(value, float) or isinstance(value, bool) or isinstance(value, int):
                    result[result_key[1:]] = value
                elif isinstance(value, dict):
                    for subkey, subvalue in value.items():
                        recurse(subkey, subvalue, result_key)

            for key in params.keys():
                value = params[key]
                recurse(key, value, '')
            return result

        futures = []
        for index, sample in enumerate(samples):
            futures.append(self.threadExecutor.submit(testSample, sample, len(self.results) + index))

        concurrent.futures.wait(futures)

        results = [future.result() for future in futures]

        for result in results:
            if self.best is None or (result['loss'] is not None and result['loss'] < self.bestLoss):
                self.bestLoss = result['loss']
                self.best = result

        self.results = self.results + results

        self.trialsSinceDetailedResults += len(results)

        if self.resultsFuture is None or self.resultsFuture.done() and len(self.results)>5:
            self.resultsFuture = self.threadExecutor.submit(lambda: self.resultsAnalyzer.outputResultsFolder(self, True))
        else:
            self.resultsAnalyzer.outputResultsFolder(self, False)


    def runOptimization(self):
        self.thread.start()

    def optimizationThread(self):
        # Make sure we output basic results if the process is killed for some reason.
        atexit.register(lambda: self.resultsAnalyzer.outputResultsFolder(self, False))
        while len(self.results) < self.totalTrials:
            self.runOptimizationRound()
        self.resultsAnalyzer.outputResultsFolder(self, True)

    def convertTrialsToResults(self, trials):
        results = []
        for trialIndex, trial in enumerate(trials.trials):
            data = {
                "trial": trialIndex,
                "status": trial['result']['status'],
                "loss": trial['result']['loss'],
                "log": "",
                "time": abs((trial['book_time'] - trial['refresh_time']).total_seconds())
            }

            params = trial['misc']['vals']
            for key in params.keys():
                if len(params[key]) == 1:
                    data[key[5:]] = json.dumps(params[key][0])
                else:
                    data[key[5:]] = ''

            results.append(data)
        return results

    def convertResultsToTrials(self, results):
        trials = hyperopt.Trials()

        for resultIndex, result in enumerate(results):
            data = {
                'book_time': datetime.datetime.now(),
                'exp_key': None,
                'misc': {'cmd': ('domain_attachment', 'FMinIter_Domain'),
                         'idxs': {},
                         'tid': resultIndex,
                         'vals': {},
                         'workdir': None},
                'owner': None,
                'refresh_time': datetime.datetime.now(),
                'result': {'loss': result['loss'], 'status': result['status']},
                'spec': None,
                'state': 2,
                'tid': resultIndex,
                'version': 0
            }

            for key in result.keys():
                if key not in self.resultInformationKeys:
                    value = result[key]
                    if value is not "":
                        data['misc']['idxs']['root.' + key] = [resultIndex]
                        data['misc']['vals']['root.' + key] = [value]
                    else:
                        data['misc']['idxs']['root.' + key] = []
                        data['misc']['vals']['root.' + key] = []

            trials.insert_trial_doc(data)
        return trials



    def exportResultsCSV(self, fileName):
        with open(fileName, 'wt') as file:
            writer = csv.DictWriter(file, fieldnames=self.results[0].keys(), dialect='unix')
            writer.writeheader()
            writer.writerows(self.results)

    def importResultsCSV(self, fileName):
        with open(fileName) as file:
            reader = csv.DictReader(file)
            results = list(reader)
            newResults = []
            for result in results:
                newResult = {}
                for key,value in result.items():
                    if value:
                        try:
                            if '.' in value or 'e' in value:
                                newResult[key] = float(value)
                            else:
                                newResult[key] = int(value)
                        except ValueError:
                            newResult[key] = value
                    elif key == 'loss':
                        newResult[key] = None
                    elif key == 'log':
                        newResult[key] = ''
                    else:
                        newResult[key] = None
                newResults.append(newResult)
            self.results = newResults
