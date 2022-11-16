# COP3410 Assignment 1
# Victor Burgos
# Date 1/30/2022

###############################
# R-1.1
# Write a short Python function, is_multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

def is_multiple(m, n):
    return True if m % n == 0 else False


print('Question 1:')
print(is_multiple(6, 3))
print(is_multiple(8, 3))


# R-1.2
# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even(k):
    return False if k & 1 else True


print('Question 2:')
print(is_even(10))
print(is_even(1))


# R-1.3
# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax(data):
    smallest = data[0]
    largest = data[0]
    for item in data:
        if item < smallest:
            smallest = item
        elif item > largest:
            largest = item
    return smallest, largest


print('Question 3:')
result = (1, 5, 7, 9, 3)
print(minmax(result))


# R-1.4
# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sum_of_squares(n):
    n -= 1
    total = 0
    while n > 0:
        total += n * n
        n -= 1
    return total


print('Question 4:')
print(sum_of_squares(7))


# R-1.6
# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def odd_sum_of_squares(n):
    n -= 1
    total = 0
    while n > 0:
        if n % 2 != 0:
            total += n * n
        n -= 1
    return total


print('Question 6:')
print(odd_sum_of_squares(7))

# R-1.9
# What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

print('Question 9:')
result = [n for n in range(50, 81, 10)]
print(result)

# R-1.10
# What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

print('Question 10:')
result = [n for n in range(-8, 9, 2)]
print(result)

# R-1.11
# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

print('Question 11:')
print([pow(2, n) for n in range(0, 9, +1)])

# Done
