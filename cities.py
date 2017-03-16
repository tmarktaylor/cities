# Copyright 2017 Mark Taylor
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import itertools
import pprint

"""
Requires Python 3.x
I saw this problem in a job posting.

The 2010 Census puts populations of 26 largest US metro areas at
 18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170,
 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809,
  3279833, 3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009,
   2149127, 2142508, and 2134411.

Can you find a subset of these areas where a total of exactly
100,000,000 people live, assuming the census estimates are exactly right?
 Provide the answer and code or reasoning used.
"""

# The problem is solved by brute force sum of all combinations of N cities.
# Where N would be 1, 2, etc.
# The list of cities is sorted from largest to smallest.
# The range of N to try is reduced.
# The problem is solved twice.
# 1. Find cities that total 100,000,000.
# 2. Find cities that total sum(cities) - 100,000,000 and choose the 
#    cities that aren't part of the solution.  These cities are removed
#    from the original set of cities.
# The initial list of cities is sorted from largest to smallest.

def fewest_cities_needed(total, items):
    """Sum largest cities first until sum exceeds total."""
    for i in range(len(items)):
        s = sum(items[:i])
        if s > total:
            return i
    return 0
   
def most_cities_needed(total, items):
    """Sum smallest cities first until sum exceeds total."""
    return fewest_cities_needed(total, sorted(items))

def solve(total, items, invert=False, 
                            number_of_combinations=None):
    """The solution can be thought of as partitioning the items into two
    sets, one whose items sum to the desired total and one that contains
    the remaining items.  When invert is True the remaining items are returned.
    
    number_of_combinations is a dictionary:
        key = length of subsequence
        value = number of combinations of subsequences of key's length
    """
    num_combinations_tried = 0
    at_least = fewest_cities_needed(total, items)
    at_most = most_cities_needed(total, items)
    print('need at least {} cities.'.format(at_least))
    print('need at most {} cities.'.format(at_most))
    assert at_least > 1, 'sanity check'
    assert at_most >= at_least, 'sanity check'
    
    # Subsequences of half the length of the city populations have
    # the most combinations and take the most time to try.
    # The test below sets the range object to try shortest subsequences first.
    if at_least < (len(items) - at_most):
        range_to_try = range(at_least, at_most + 1)
    else:
        range_to_try = range(at_most, at_least - 1, -1)  # 
        
    fmt = 'trying {} combinations of {} cities.'
    for x in range_to_try:
        if number_of_combinations:
            n = number_of_combinations[x]
            print('trying {} combinations of {} cities.'.format(n, x))
            num_combinations_tried += n
        else:
            print('trying combinations of {} cities.'.format(x))        
            
        combs = itertools.combinations(items, x)
        for comb in combs:
            if sum(comb) == total:   # solved?

            # yes-
                if number_of_combinations:
                    fmt = 'Tried {} combinations.'
                    print(fmt.format(num_combinations_tried))
                if invert:
                    comb = set(items) - set(comb)
                return comb
    return False

def calculate_numbers_of_combinations_of(a_sequence):
    """Return dict key= subsequence length, value= number of combinations)."""
    number_of_combinations = dict()
    for at_a_time, _ in enumerate(a_sequence, start=1):
        n = len(a_sequence)
        subsequences = itertools.combinations(a_sequence, at_a_time)

        # This requires less memory than 
        # subsequence_length = len(list(combinations))
        # and should run faster.
        subsequence_length = 0
        for comb in subsequences: 
            subsequence_length += 1
        number_of_combinations[at_a_time] = subsequence_length
    return number_of_combinations


if __name__ == '__main__':
    pp = pprint.PrettyPrinter(width=79, compact=True)
    city_populations = [18897109, 12828837, 9461105, 6371773, 5965343, 
                        5946800,   5582170, 5564635, 5268860, 4552402,
                        4335391,   4296250, 4224851, 4192887, 3439809,
                        3279833,   3095313, 2812896, 2783243, 2710489,
                        2543482,   2356285, 2226009, 2149127, 2142508,
                        2134411]
    ONE_HUNDRED_MILLION = 100000000
    
    print('Can you find a subset of these areas where a total of exactly')
    print('100,000,000 people live?')
    print('City Populations:')
    pp.pprint(city_populations)

    # Determine numbers of combinations of subsequences of city_populations.
    print('Calulating the numbers of combinations.')
    print('This takes a few seconds, but should be less than a minute. ...')
    combinations = calculate_numbers_of_combinations_of(city_populations)
    fmt = 'combinations of {} taken {} at a time = {}'
    n = len(city_populations)
    for at_a_time, _ in enumerate(city_populations, start=1):
        print(fmt.format(n, at_a_time, combinations[at_a_time]))
    
    for invert_solution in (False, True):
        if invert_solution:
            target_total = sum(city_populations) - ONE_HUNDRED_MILLION
        else:
            target_total = ONE_HUNDRED_MILLION
        print('---------------------------------------------------------')
        print('Choose integers that total {}'.format(target_total))
        start_time = time.perf_counter()
        solution = solve(target_total, 
                         city_populations,
                         invert_solution,
                         combinations)
        end_time = time.perf_counter()
        print()
        if solution:
            print('Solved.')
            print('Number of cities is {}'.format(len(solution)))
            print('Sum of cities is {}'.format(sum(solution)))
            print('solution...')
            solution_list = list(solution)
            if invert_solution:
                solution_list = sorted(solution_list, reverse=True)
            pp.pprint(solution_list)
        else:
            print('could not solve')
        print('elapsed time', end_time - start_time)

