Write a Python function frequency(l) that takes as input a list of integers and returns a pair of the form (minfreqlist,maxfreqlist) where

a)minfreqlist is a list of numbers with minimum frequency in l, sorted in ascending order
b)maxfreqlist is a list of numbers with maximum frequency in l, sorted in ascending 

For instance:
```
>>> frequency([13,12,11,13,14,13,7,11,13,14,12])
([7], [13])

>>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14])
([7], [13, 14])

>>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7])
([7, 11, 12], [13, 14])
```
