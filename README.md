Solve select city population that total exactly 100,000,000 problem.

Requires Python 3.x.

I saw this problem in a job posting.

```
The 2010 Census puts populations of 26 largest US metro areas at 18897109,
 12828837, 9461105, 6371773, 5965343, 5946800, 5582170, 5564635, 5268860,
 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833, 3095313,
 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508,
 and 2134411.
 Can you find a subset of these areas where a total of exactly 100,000,000
 people live, assuming the census estimates are exactly right?"
``` 
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

Here is another snippet with the fenced code block info string of python3.

```python3
def show_numbers_of_combinations_of(a_sequence):
    """Print the number of combinations for subsequences."""
    print('Show the number of combinations and the total number of')
    print('additions to sum all the combinations.')
    for at_a_time, _ in enumerate(a_sequence, start=1):
        n = len(a_sequence)
        subsequences = itertools.combinations(a_sequence, at_a_time)

        fmt = 'combinations of {} taken {:2} at a time = {:10,}, adds= {:11,}'

        # This requires less memory than 
        # subsequence_length = len(list(combinations))
        # and should run faster.
        num_subsequences = 0
        for _ in subsequences: 
            num_subsequences += 1
        print(fmt.format(n, at_a_time, num_subsequences, 
                        (at_a_time - 1) * num_subsequences))
```
