# COP3410 Assignment 5
# Victor Burgos
# Date 3/14/2022

###################################
# 1- Compute the sum of all numbers in an n×n data set, represented as a list of lists.

data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

res = list()
for j in range(0, len(data[0])):
    tmp = 0
    for i in range(0, len(data)):
        tmp = tmp + data[i][j]
    res.append(tmp)

print("Question 1 = ", str(res))

# 2- Use the built-in sum function combined with Python’s comprehension syntax to compute the sum of all numbers in
# an n×n data set, represented as a list of lists.

res = [sum(x) for x in zip(*data)]
print("Question 2 = ", res)

# 3- The shuffle method, supported by the random module, takes a Python list, and rearranges it so
# that every possible ordering is equally likely. Implement your own version of such a function.
# You may rely on the randrange(n) function of the random module, which returns a random
# number between 0 and n−1 inclusive.

import random

newlist = [2, 6, 7, 9, 10]
res = random.sample(newlist, len(newlist))

print("Question 3 = ", str(res))

# 4- Let B be an array of size n ≥ 6 containing integers from 1 to n, inclusive, with exactly five
# repeated. Write a function that finds the unique value in the array.

B = [1, 2, 3, 2, 4, 2, 5, 2, 6, 2]

for i in range(0, len(B)):
    for j in range(i + 1, len(B)):
        if B[i] == B[j]:
            print  # had an issue ending the function so just put print

print("Question 4 = ", B[j])
