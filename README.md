# GIT-Activity
GIT activity for COMET probationary members from GIT workshop on Sept 24, 2018

This basic activity should teach the probies basic version control with git with an activity of python

The probies should make a python script that can print 3 shapes

They should collaborate by working on these empty methods:

```python

def make_sqaure(size):
    pass

def make_rectangle(length, width):
    pass

def make_triangle(size):
    pass
```

the main method would ask them of the shape then depending on the shape, should ask for extra parameters
```
Hello, please enter what to print
1       square
2       rectangle
3       triangle
Input:
```
The input for the shape and extra parameters are already given so given the shape, it should print in these following patterns:

## Square
given an input **size** the method should print a square  in sizexsize
```
Input: 1
Input size:6
******
******
******
******
******
******
```

## Rectangle
given an input **length** and **width** the method should print a rectangle  in lengthxwidth size
```
Input: 2
Input length: 6
Input width: 4
****
****
****
****
****
****
```

## Triangle
given an input **size** the method should print a triangle  in this pattern:

```
Input: 3
Input size: 5
....*....
...***...
..*****..
.*******.
*********
```
