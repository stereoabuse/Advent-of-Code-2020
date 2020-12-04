# Advent of Code 2020

Goals for this year include learning git, PyCharm, regex edge-cases.
                             
### [Day 01](solutions/day_01.py)
I solved this with a naive double or triple for-loop, checking to make sure that the values for each entry was unique and returning the product when the two loops found the right sum.

### [Day 02](solutions/day_02.py)
Slowest part for me was parsing the input text.  Added a new function to my utilities that splits each line into its [alphanum chunks](https://github.com/stereoabuse/Advent-of-Code-2020/blob/45c0c33d0ede292e2cd8a07e5b360052cb1ad8c8/solutions/utils.py#L52) to prevent this issue next time. Also had an off-by-one error from increasing instead of decreasing the index by 1.

### [Day 03](solutions/day_03.py)
Problem itself was straightforward.  Start looping through row and column indexes by the slope and check each time if it has a `#`.  Another Python index error today where I swapped rows and columns in the slope for a few minutes before catching it.

### [Day 04](solutions/day_04.py)
Finished part 1 in 360th place.  Part 2 ... not so lucky.  There turned out to be missing an edge case where `(?!\S)` was needed at the end of `r'(pid:\d{9})'` to stop a 10-digit pid getting through.  So that took me a couple hours, a meal, and a full night of sleep to find.  Adding regex-fu to goals now.