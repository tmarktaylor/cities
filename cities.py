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
# The problem sum(cities) - 100,000,000 is solved first which gives the 
# cities that aren't part of the solution.  These cities are removed
# from the original set of cities.
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

def solve_combinations_list(total, items, invert=False):
    """The term invert denotes the concept that the original set is partitioned
    into two sets, one whose items sum to the desired total and one that
    contains the remaining items. When 'inverting' the remaining items are
    returned.
    """

    atleast = fewest_cities_needed(total, items)
    atmost = most_cities_needed(total, items)
    print('need at least {} cities.'.format(atleast))
    print('need at most {} cities.'.format(atmost))
    for x in range(atleast, atmost+1):
        print('trying combinations of {} cities.'.format(x))
        combs = itertools.combinations(items, x)
        for comb in combs:
            if sum(comb) == total:
                if invert:
                    comb = set(items) - set(comb)
                return comb
    return False


if __name__ == '__main__':
    pp = pprint.PrettyPrinter(width=79, compact=True)
    availlist = [18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170,
                  5564635,  5268860, 4552402, 4335391, 4296250, 4224851, 4192887,
                  3439809,  3279833, 3095313, 2812896, 2783243, 2710489, 2543482,
                  2356285,  2226009, 2149127, 2142508, 2134411]
    m100 = 100000000
    print('choose positive integers from...')
    pp.pprint(availlist)
    for invert_solution in (False, True):
        if invert_solution:
            targettotal = sum(availlist) - m100
        else:
            targettotal = m100
        print('---------------------------------------------------------')
        print('Choose integers that total {}'.format(targettotal))
        start_time = time.perf_counter()
        solution = solve_combinations_list(targettotal, availlist, invert_solution)
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

