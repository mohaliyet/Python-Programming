# Module 01: Advanced Data Structures

## Lesson 01: Nested Lists and Comprehensions

### Goal and Objectives

#### Goal
The goal of this video is to introduce you to nested lists and list comprehensions in Python. By the end of this video, you will understand how to create and manipulate nested lists and use list comprehensions to create lists in a concise and readable manner.

#### Objectives
- Understand what nested lists are and how to create them.
- Learn how to access and manipulate elements in nested lists.
- Understand the concept of list comprehensions.
- Learn how to use list comprehensions to create lists.
- Explore nested and conditional list comprehensions.

### Introduction to Nested Lists

#### What are Nested Lists?

Nested lists are lists within lists. They are useful for representing matrices or grids. Let's explore how to create and access elements in nested lists.

**Example of a Nested List:**

```python
# Creating a nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print(matrix[0][1])  # Output: 2
```
In this example, matrix is a nested list with three sublists. Each sublist represents a row in the matrix. To access an element, you use two indices: the first for the row and the second for the column.

### List Comprehensions
List comprehensions provide a concise way to create lists. They are more readable and often faster than traditional loops.

### Basic List Comprehension
### Example of a Basic List Comprehension:
```python
# Creating a list of squares using a list comprehension
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
In this example, the list comprehension [x**2 for x in range(10)] creates a list of squares for numbers from 0 to 9.

### Nested List Comprehension
You can also use list comprehensions with nested lists.

### Example of a Nested List Comprehension:

```python 
# Flattening a nested list using a nested list comprehension
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

In this example, the nested list comprehension [item for sublist in nested_list for item in sublist] flattens the nested list into a single list.

### Conditional List Comprehension
You can add conditions to list comprehensions to filter elements.

### Example of a Conditional List Comprehension:

```python 
# Creating a list of even squares using a conditional list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]
```
In this example, the list comprehension `[x**2 for x in range(10) if x % 2 == 0]` creates a list of squares for even numbers from 0 to 9.
### Summary
By understanding nested lists and list comprehensions, you can create and manipulate complex data structures in a concise and readable manner. Practice using these concepts to become proficient in handling lists in Python.


