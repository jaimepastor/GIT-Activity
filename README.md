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
Some additional functions you may need to know:
Inputs are written in main() and output should be written in their respective methods
There is actually no need to change the main method anymore

the **range(x, y)** method returns you a list from x to y exclusive of y
for example
```python
range(4, 12)
##this returns you a list of [4,5,6,7,8,9,10,11]
```
the **input('string')**  the input would print the string  parameter and returns you a string from the input of the user
for example
```python
input('enter your name:')
##this would print 'enter your name:' and wait for the input of the user
##if the user inputs something like this 'enter your name: John' it returns to you the string John
```

More python knowledge you need to know to complete this activity: [conditions](https://www.w3schools.com/python/python_conditions.asp) and [loops](https://www.w3schools.com/python/python_for_loops.asp)
