'''
synbiochem (c) University of Manchester 2015

synbiochem is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
# pylint: disable=too-many-arguments
import math
import random
import traceback

from synbiochem.utils.job import JobThread


class SimulatedAnnealer(JobThread):
    '''Class to perform simulated annealing method.'''

    def __init__(self, solution, acceptance=0.01, max_iter=10000,
                 heartbeat=1, verbose=False):
        self.__solution = solution
        self.__acceptance = acceptance
        self.__max_iter = max_iter
        self.__verbose = verbose
        self.__heartbeat = heartbeat
        JobThread.__init__(self)

    def run(self):
        '''Optimises a solution with simulated annealing.'''
        if self.__init():
            # Initialization:
            iteration = 0
            accepts = 0
            rejects = 0
            r_temp = 0.025
            cooling_rate = r_temp / 100

            energy = self.__solution.get_energy()

            while not self._cancelled \
                    and energy > self.__acceptance \
                    and iteration < self.__max_iter:
                iteration += 1
                energy_new = self.__solution.mutate()

                if energy_new < energy:
                    # Accept move immediately:
                    energy = energy_new
                    self.__accept(iteration)
                    print '\t'.join(['T', str(iteration), str(energy_new),
                                     str(self.__solution)])
                elif energy_new == energy:
                    # Reject move:
                    self.__solution.reject()
                    rejects += 1
                    print '\t'.join([' ', str(iteration), str(energy_new),
                                     str(self.__solution)])
                elif math.exp((energy - energy_new) / r_temp) > \
                        random.random():
                    # Accept move based on conditional probability:
                    energy = energy_new
                    self.__accept(iteration)
                    accepts += 1
                    print '\t'.join(['*', str(iteration), str(energy_new),
                                     str(self.__solution)])
                else:
                    # Reject move:
                    self.__solution.reject()
                    rejects += 1
                    print '\t'.join([' ', str(iteration), str(energy_new),
                                     str(self.__solution)])

                # Heartbeat:
                self.__check_heartbeat(iteration)

                # Simulated annealing control:
                if accepts + rejects > 50:
                    if float(accepts) / float(accepts + rejects) > 0.2:
                        # Too many accepts, reduce r_temp:
                        r_temp /= 2.0
                        accepts = 0
                        rejects = 0
                    elif float(accepts) / float(accepts + rejects) < 0.01:
                        # Too many rejects, increase r_temp:
                        r_temp *= 2.0
                        accepts = 0
                        rejects = 0

                r_temp *= 1 - cooling_rate

            if iteration == self.__max_iter:
                message = 'Unable to optimise in ' + str(self.__max_iter) + \
                    ' iterations'
                self.__fire_event('error', 100, iteration, message=message)
            elif self._cancelled:
                self.__fire_event('cancelled', 100, iteration,
                                  message='Job cancelled')
            else:
                self.__fire_event('finished', 100, iteration,
                                  message='Job completed')

    def __init(self):
        '''Initialise.'''
        self.__fire_event('running', 0, 0, message='Job initialising...')

        try:
            self.__solution.init()
        except ValueError:
            self.__fire_event('error', 100, 0, message=traceback.format_exc())
            return False

        self.__fire_event('running', 0, 0, message='Job initialised')
        return True

    def __check_heartbeat(self, iteration):
        '''Heartbeat.'''
        if float(iteration) % self.__heartbeat == 0:
            self.__fire_event('running',
                              float(iteration) / self.__max_iter * 100,
                              iteration,
                              'Running...')

    def __accept(self, iteration):
        '''Accept the current solution.'''
        self.__solution.accept()

        self.__fire_event('running', float(iteration) / self.__max_iter * 100,
                          iteration, 'Running...')

    def __fire_event(self, status, progress, iteration, message=''):
        '''Fires an event.'''
        event = {'update': {'status': status,
                            'message': message,
                            'progress': progress,
                            'iteration': iteration,
                            'max_iter': self.__max_iter,
                            'values': self.__solution.get_values()},
                 'query': self.__solution.get_query()
                 }

        if status == 'finished':
            event['result'] = self.__solution.get_result()

        self._fire_event(event)
