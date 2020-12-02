# Advent of Code 2020

Goals for this year include learning git and PyCharm.
                             
                             
### [Day 01](solutions/day_01.py)
I solved this with a naive double or triple for-loop, checking to make sure that 
the values for each entry was unique and returning the product when the two loops found the right sum.

### [Day 02](solutions/day_02.py)
Slowest part for me was parsing.  Adding a new function to my utilities that splits each line in alphanum chunks.  Also had off by one error with indexes where I increased the index offset rather than decreased by one.
Too much time working with indexes in only Python.