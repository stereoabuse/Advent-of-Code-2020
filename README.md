# Advent of Code 2020

Goals for this year include learning git and PyCharm.
                             
### [Day 01](solutions/day_01.py)
I solved this with a naive double or triple for-loop, checking to make sure that the values for each entry was unique and returning the product when the two loops found the right sum.

### [Day 02](solutions/day_02.py)
Slowest part for me was parsing.  Adding a new function to my utilities that splits each line into its [alphanum chunks](https://github.com/stereoabuse/Advent-of-Code-2020/blob/45c0c33d0ede292e2cd8a07e5b360052cb1ad8c8/solutions/utils.py#L52) will prevent this issue next time. Also had an off-by-one error from increasing instead of decreasing the index by 1.