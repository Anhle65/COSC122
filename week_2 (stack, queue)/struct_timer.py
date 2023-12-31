import sys
import random
import time
from stack import Stack
from queue122 import Queue
from deque import Deque


print("Using time.perf_counter for timing.")
REZ = time.get_clock_info('perf_counter').resolution
print('Smallest unit of time is ' + str(REZ) + ' seconds')


def time_stack_push(initial_size, n_trials):
    """ Finds average time for pushing onto a stack of a given initial size"""
    s = Stack()

    # s._data = [0] * initial_size  # is cunning but sometimes causes weird timings
    # so simply push lots of random items onto the stack
    for _ in range(initial_size):
        s.push(random.randint(0, 127))

    # time some pushes
    start_time = time.perf_counter()
    for i in range(n_trials):
        s.push(0)
    end_time = time.perf_counter()
    time_per_operation = (end_time - start_time)/n_trials

    template = "Initial Stack size = {:,d} -> avg. time/push for {:,d} pushes is {:10.8f}"
    print((template.format(initial_size, n_trials, time_per_operation)))
    return s


# Do some creative copy and pasting here to make functions for other time trials
# ---start student section---
def time_stack_pop(initial_size, n_trials):
    """ Finds average time for pushing onto a stack of a given initial size"""

    # s._data = [0] * initial_size  # is cunning but sometimes causes weird timings
    # so simply push lots of random items onto the stack
    # for _ in range(initial_size):
    #     s.pop()

    # time some pushes
    start_time = time.perf_counter()
    for i in range(n_trials):
        initial_size.pop()
    end_time = time.perf_counter()
    time_per_operation = (end_time - start_time)/n_trials

    template = "Initial Stack size = {:,d} -> avg. time/pop for {:,d} pops is {:10.8f}"
    print((template.format(len(initial_size), n_trials, time_per_operation)))
# ===end student section===


def run_tests():
    """ Runs as many or as few tests as you call,
    initially just runs the test for stack pushes
    """
    print('\n' *3)
    initial_size = 100000  # start with this many items in data structure
    n_trials = 100  # run this many trials and take the average time

    a = time_stack_push(initial_size, n_trials)
    time_stack_pop(a, n_trials)

    # call your shiny new test functions here


run_tests()
