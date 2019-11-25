A square n×n matrix of integers can be written in Python as a list with n elements, where each element is in turn a list of n integers, representing a row of the matrix. For instance, the matrix
```
  1  2  3
  4  5  6
  7  8  9
 ``` 
would be represented as ```[[1,2,3], [4,5,6], [7,8,9]].```

Write a function rotate(m) that takes a list representation m of a square matrix as input, and returns the matrix obtained by rotating the original matrix clockwize by 90 degrees. For instance, if we rotate the matrix above, we get
```
  7  4  1
  8  5  2
  9  6  3
```
Your function should not modify the argument m provided to the function rotate().

Here are some examples of how your function should work.

 ```
  >>> rotate([[1,2],[3,4]])
  [[3, 1], [4, 2]]
```
Explanation:
```
     1  2    becomes     3  1
     3  4                4  2
  ```

``` 
  >>> rotate([[1,2,3],[4,5,6],[7,8,9]])
  [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```
Explanation:
```
     1  2  3    becomes   7  4  1
     4  5  6              8  5  2
     7  8  9              9  6  3
 ``` 
```
  >>> rotate([[1,1,1],[2,2,2],[3,3,3]])
  [[3, 2, 1], [3, 2, 1], [3, 2, 1]]
```
Explanation:
```
     1  1  1    becomes   3  2  1
     2  2  2              3  2  1
     3  3  3              3  2  1
 ``` 

