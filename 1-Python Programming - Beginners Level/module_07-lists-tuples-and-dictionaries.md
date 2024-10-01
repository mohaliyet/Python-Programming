# Module 7: Lists, Tuples, and Dictionaries

## Goal and Objectives

### Goal

The goal of this module is to introduce you to three fundamental data structures in Python: lists, tuples, and dictionaries. By the end of this module, you will be able to create, manipulate, and use these data structures effectively.

### Objectives

- Learn how to create and manipulate lists.
- Understand the differences between lists and tuples.
- Learn how to create and use tuples.
- Understand how to create and manipulate dictionaries.

## Working with Lists

### Creating Lists and Accessing Elements

Lists are ordered collections of items that are mutable.

- Creating a List

  ```python
  fruits = ["apple", "banana", "cherry"]
  ```
- Accessing Elements (Indexing)

  ```python
  print(fruits[0])  # apple
  ```
- Slicing

  ```python
  print(fruits[1:3])  # ['banana', 'cherry']
  ```

### Common List Methods

Lists have several built-in methods for common operations.

- `.append()`: Adds an element to the end of the list

  ```python
  fruits.append("date")
  print(fruits)  # ['apple', 'banana', 'cherry', 'date']
  ```
- `.remove()`: Removes the first occurrence of an element

  ```python
  fruits.remove("banana")
  print(fruits)  # ['apple', 'cherry', 'date']
  ```
- `.sort()`: Sorts the list in ascending order

  ```python
  fruits.sort()
  print(fruits)  # ['apple', 'cherry', 'date']
  ```
- `.reverse()`: Reverses the order of the list

  ```python
  fruits.reverse()
  print(fruits)  # ['date', 'cherry', 'apple']
  ```

### List Comprehensions

List comprehensions provide a concise way to create lists.

- Basic List Comprehension
  ```python
  squares = [x**2 for x in range(5)]
  print(squares)  # [0, 1, 4, 9, 16]
  ```

### Nested Lists

Lists can contain other lists as elements.

- Creating a Nested List

  ```python
  matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
  ]
  ```
- Accessing Elements in a Nested List

  ```python
  print(matrix[0][1])  # 2
  ```

## Tuples

### Differences Between Lists and Tuples

Tuples are similar to lists but are immutable, meaning their elements cannot be changed after creation.

### Creating and Accessing Tuples

- Creating a Tuple

  ```python
  fruits = ("apple", "banana", "cherry")
  ```
- Accessing Elements

  ```python
  print(fruits[0])  # apple
  ```

### Tuple Packing and Unpacking

- Packing a Tuple

  ```python
  fruit_tuple = "apple", "banana", "cherry"
  ```
- Unpacking a Tuple

  ```python
  apple, banana, cherry = fruit_tuple
  print(apple)  # apple
  ```

## Dictionaries (Introduction)

### Creating Dictionaries

Dictionaries are collections of key-value pairs.

- Creating a Dictionary
  ```python
  student = {
      "name": "Alice",
      "age": 25,
      "courses": ["Math", "Science"]
  }
  ```

### Accessing and Modifying Key-Value Pairs

- Accessing Values

  ```python
  print(student["name"])  # Alice
  ```
- Modifying Values

  ```python
  student["age"] = 26
  print(student["age"])  # 26
  ```

### Common Dictionary Methods

Dictionaries have several built-in methods for common operations.

- `.keys()`: Returns a list of all keys

  ```python
  print(student.keys())  # dict_keys(['name', 'age', 'courses'])
  ```
- `.values()`: Returns a list of all values

  ```python
  print(student.values())  # dict_values(['Alice', 26, ['Math', 'Science']])
  ```
- `.items()`: Returns a list of all key-value pairs

  ```python
  print(student.items())  # dict_items([('name', 'Alice'), ('age', 26), ('courses', ['Math', 'Science'])])
  ```
