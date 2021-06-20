Solve select city population that total exactly 100,000,000 problem.
Requires Python 3.x.
I saw this problem in a job posting.
"The 2010 Census puts populations of 26 largest US metro areas at 18897109,
 12828837, 9461105, 6371773, 5965343, 5946800, 5582170, 5564635, 5268860,
 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833, 3095313,
 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508,
 and 2134411.
 Can you find a subset of these areas where a total of exactly 100,000,000
 people live, assuming the census estimates are exactly right?"
 
 Here is the guts of the solution in cities.py.
 
 ```python
 def solve(total, items, invert=False): 
    """The solution can be thought of as partitioning the items into two
    sets, one whose items sum to the desired total and one that contains
    the remaining items.  When invert is True the remaining items are returned.
    """
    num_combinations_tried = 0
    num_adds = 0
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
        
    for x in range_to_try:
        print('Trying combinations of {} cities.'.format(x))
        combs = itertools.combinations(items, x)
        for comb in combs:
            num_combinations_tried += 1   # increases solution time slightly
            num_adds += (x - 1)
            if sum(comb) == total:   # solved?

                # yes-
                print('Tried {:,} combinations.'.format(num_combinations_tried))
                print('Number of additions = {:,}.'.format(num_adds))
                if invert:
                    comb = set(items) - set(comb)
                return comb
    return False
```    
