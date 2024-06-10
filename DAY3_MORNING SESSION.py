# Arithmetic Operators
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333...
print(a % b)  # Output: 1
print(a ** b) # Output: 1000
print(a // b) # Output: 3

# Assignment Operators
a += b  # a = a + b
print(a)  # Output: 13

# Comparison Operators
print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: True
print(a < b)   # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False

# Logical Operators
print(a > 5 and b < 5)  # Output: True
print(a > 5 or b > 5)   # Output: True
print(not (a > 5))      # Output: False

# Bitwise Operators
print(a & b)  # Output: 1
print(a | b)  # Output: 15
print(a ^ b)  # Output: 14
print(~a)     # Output: -14
print(a << 1) # Output: 26
print(a >> 1) # Output: 6

# Membership Operators
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)       # Output: True
print(6 not in numbers)   # Output: True

# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)       # Output: True
print(x is y)       # Output: False
print(x == y)       # Output: True
print(x is not y)   # Output: True


# LISTS  AND DICTIONARY COMPREHESION.
# Lists in Python
# Definition:
# A list in Python is an ordered collection of elements that can be of different types 
# (e.g., integers, strings, or other lists). Lists are mutable, meaning their elements 
# can be changed after they are created.
# Creating and modifying a list in less than three lines
fruits = ["apple", "banana", "cherry"]; fruits.append("date"); print(fruits)


# EXERCISE
# List comprehension to generate squares of even numbers in the range of 20
even_squares = [x**2 for x in range(2, 21, 2)]

print(even_squares)

# DICTIONARY
# Python, a dictionary is an unordered collection of key-value pairs. 
# Each key-value pair maps the key to its associated value. Dictionaries are mutable, meaning they can be modified after creation.
# Keys within a dictionary must be unique and immutable, such as strings, numbers, or tuples.
# Dictionary example 
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
print(my_dict)

# EXERCISE
# CREate list of tuple where each tuple contains number and 
# its cude of numbers between 1 and 8 using dictionary comprehension
# List of tuples using dictionary comprehension
list_of_tuples = [(x, x**3) for x in range(1, 9)]

print(list_of_tuples)
