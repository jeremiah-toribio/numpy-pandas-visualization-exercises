import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a) / len(a)
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
prod_of_a = 1
for i in a:
    prod_of_a *= i
prod_of_a
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [i ** 2 for i in a]
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
def odds_of_a(lis):
    alist = []
    for i in a:
        if i % 2 != 0:
            alist.append(i)
    return alist
print(odds_of_a(a))
odds_in_a = odds_of_a(a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
def evens_of_a(lis):
    alist = []
    for i in a:
        if i % 2 == 0:
            alist.append(i)
    return alist
print(evens_of_a(a))
## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
b = np.array(b)
sum_of_b = b.sum()

# Exercise 2 - refactor the following to use numpy. 
min_of_b = b.min()

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = b.max()

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = b.mean()

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = b * b
# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = b ** 2


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = b % 2 != 0

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = b % 2 == 0

# Exercise 9 - print out the shape of the array b.
b.shape()
# Exercise 10 - transpose the array b.
b.transpose()
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
list_b = np.reshape(b, -1)
list_b.tolist()
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
list_bb = np.reshape(b,(6,1))
list_bb.tolist()
## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c = np.array(c)
c.min()
c.max()
c.sum()
np.prod(c)

x = []
y
# Exercise 2 - Determine the standard deviation of c.
c.std()
# Exercise 3 - Determine the variance of c.
np.var(c)
# Exercise 4 - Print out the shape of the array c
c.shape()
# Exercise 5 - Transpose c and print out transposed result.
print(c.transpose())
# Exercise 6 - Get the dot product of the array c with c. 
np.dot(c,c)
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
product_c = c*c
c.sum() + c.transposed()
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
tranc = c.transposed()
c * tranc

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

np.array(d)
# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)
# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)
# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)
# Exercise 4 - Find all the negative numbers in d
d % 2 != 0
# Exercise 5 - Find all the positive numbers in d
d % 2 == 0
# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)
# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))
np.unique(d).size
# Exercise 8 - Print out the shape of d.
d.shape()
# Exercise 9 - Transpose and then print out the shape of d.
d.transpose().shape
# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9,2)