# Pyramid Path Finder with Maximum Sum
A program written in Python to traverse any given pyramid-shaped integers from top to bottom and find the path with maximum sum without visiting any prime number.

## General Information
This program requires orthogonal triangle-shaped integers in an input text file and reads it, then traverses this pyramid-shaped data from the first element at the top to any last element at the bottom, only downwards and rightwards without visiting any prime numbers to find the path with the maximum sum of the visited values.

There will be orthogonal triangle-shaped integers given in a file to find the path of the maximum sum of numbers from top to bottom by the given rules below:

input:
```
215
193 124
117 237 442
218 935 347 235
320 804 522 417 345
229 601 723 835 133 124
248 202 277 433 207 263 257
359 464 504 528 516 716 871 182
461 441 426 656 863 560 380 171 923
381 348 573 533 447 632 387 176 975 449
223 711 445 645 245 543 931 532 937 541 444
330 131 333 928 377 733 017 778 839 168 197 197
131 171 522 137 217 224 291 413 528 520 227 229 928
223 626 034 683 839 053 627 310 713 999 629 817 410 121
924 622 911 233 325 139 721 218 253 223 107 233 230 124 233
```
---

1) You will start from the top and move only downwards diagonally to an adjacent number.
2) You cannot visit any PRIME number, the path must only have NON-PRIME numbers.
3) You have to reach the bottom of the pyramid with the highest sum of visited numbers.
4) You must treat the input as a pyramid of integers.
* By using these rules, find the path from top to bottom with the maximum sum of numbers.

## Simple Example:

```
10
12 16
14 13 15
21 19 20 18
```
This is equivalent to:
```
      10
    12  16
  14  13  15
21  19  20  18
```

Starting from the top (10) and without visiting any prime numbers, there are those possible paths:
```
10 => 16 => 15 => 18:     Sum = 59
10 => 16 => 15 => 20:     Sum = 61(*) The Path of Maximum Sum
10 => 16 => 13(X)         Prime Number Blocks the Path!
10 => 12 => 13(X)         Prime Number Blocks the Path!
10 => 12 => 14 => 19(X)   Prime Number Blocks the Path!
10 => 12 => 14 => 21:     Sum = 57
```
```
     (10)
    12 (16)
  14  13 (15)
21  19 (20) 18
```
```
10 => 16 => 15 => 20:   The Path of Maximum Sum (61)
```

## Setup & Run
There are 2 different files to run the main program in different ways:
1. **Pyramid_Max_Path.ipynb** has all the steps of the program, which can be run with Jupyter Notebook:
```
pip install jupyter
```
```
jupyter notebook
```
2. **Pyramid_Max_Path.py** file can be run directly with Python:
```
python Pyramid_Max_Path.py input txt
```
* The input file is given as **input.txt**, which must be given as the command line argument or the input filename string at runtime.
* **Generate_Pyramid.py** generates a new input file named **random_pyramid.txt** to test the program with randomly generated new numbers:
```
python Generate_Pyramid.py
```
```
python Pyramid_Max_Path.py random_pyramid txt
```
* In **Pyramid_Max_Path.ipynb**, there is a section that replaces 2 numbers of the second line from top of the pyramid with 2 prime numbers, which block all the possible pathways from top to bottom. This blocked pyramid data is written in **random_pyramid_blocked.txt** file to show that the program will not be able to find any path with maximum sum if the prime numbers block them all. Python version:
```
python Block_Pyramid.py
```
```
python Pyramid_Max_Path.py random_pyramid_blocked txt
```