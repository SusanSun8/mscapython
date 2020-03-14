# mscapython
msca python assignment 3/ Final Project 
by Xiangwen Sun

## Installation

1. python setup.py install

## Base use

* First, after we install the package, we can see a base in the directory (import mscapython)
* There are two functions in the base, as we can assess by mscapython.base.hello() and mscapython.base.salad()
* The hello function print "Hello World!"
* The salad class has two functions read and write
* read takes in three variables (path, salad list, number list), in which path is a file path, salad is a list of ingredients in the salad, and the number list is the number of each ingredient in the salad. The length of two list should matches. 
* read's output would be ingredientXX.salad, where"XX" is the number. 
* write takes in a path, and find all the ".salad" files in that path
* write then output a dictionary with {ingredient1: #num, ingredient2: #num}

## Salad timing

* The performance for salad is almost zero but dependent on the input salad length. 
