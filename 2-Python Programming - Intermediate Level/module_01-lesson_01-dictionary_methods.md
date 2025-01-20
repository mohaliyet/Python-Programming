# Module 01: Advanced Data Structures

## Lesson 02: Advanced Dictionary Methods

### Goal and Objectives

#### Goal

The goal of this lesson is to introduce you to advanced dictionary methods in Python. By the end of this lesson, you will understand how to use methods like `get()`, `setdefault()`, and `.update()` to manipulate dictionaries effectively.

#### Objectives

- Understand the use of the `get()` method.
- Learn how to use the `setdefault()` method.
- Explore the `.update()` method for updating dictionaries.

### Advanced Dictionary Methods

#### Using the `get()` Method

The `get()` method returns the value for a specified key if the key is in the dictionary. If the key is not found, it returns a default value.

**Example of `get()` Method:**

```python
# Using the get() method
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('b', 0)
print(value)  # Output: 2

# Using get() with a default value
value = my_dict.get('d', 0)
print(value)  # Output: 0
```

In this example, `my_dict.get('b', 0)` returns the value associated with the key 'b'. If the key is not found, it returns the default value 0.

#### Using the `setdefault()` Method

The `setdefault()` method returns the value of a key if it is in the dictionary. If not, it inserts the key with a specified value.

**Example of `setdefault()` Method:**

```python
# Using the setdefault() method
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.setdefault('b', 0)
print(value)  # Output: 2

# Using setdefault() to add a new key
value = my_dict.setdefault('d', 4)
print(value)  # Output: 4
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

In this example, `my_dict.setdefault('b', 0)` returns the value associated with the key 'b'. If the key 'd' is not found, it adds 'd' with the value 4 to the dictionary.

#### Using the `.update()` Method

The `.update()` method updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs.

**Example of `.update()` Method:**

```python
# Using the update() method
my_dict = {'a': 1, 'b': 2}
my_dict.update({'b': 3, 'c': 4})
print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Using update() with an iterable of key-value pairs
my_dict.update([('d', 5), ('e', 6)])
print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 6}
```

In this example, `my_dict.update({'b': 3, 'c': 4})` updates the value of 'b' to 3 and adds a new key 'c' with the value 4. The second update adds keys 'd' and 'e' with their respective values.

### Summary

By understanding and using advanced dictionary methods like `get()`, `setdefault()`, and `.update()`, you can manipulate dictionaries more effectively in Python. Practice using these methods to become proficient in handling dictionaries.
