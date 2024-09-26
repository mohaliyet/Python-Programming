# Module 3: Input/Output and String Manipulation

## Goal and Objectives

### Goal
The goal of this module is to introduce you to input and output operations in Python, as well as string manipulation techniques. By the end of this module, you will be able to take input from users, display output, and perform various operations on strings.

### Objectives
- Learn how to take input from the user using `input()`.
- Understand how to print output using `print()`.
- Explore different string formatting methods: `f-strings`, `.format()`.
- Learn string `indexing` and `slicing`.
- Use common string methods: `.upper()`, `.lower()`, `.replace()`, `.split()`.
- Perform concatenation and replication of strings.

## Input and Output

### Taking Input from the User
In Python, you can take input from the user using the `input()` function. The input is always returned as a string.

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```
### Printing Output
You can display output using the `print()` function. It can take multiple arguments and automatically adds a space between them.

## String Formatting
String formatting allows you to create strings with dynamic content. There are several ways to format strings in Python:
**f-strings (Python 3.6+)** - f-strings provide a concise and readable way to embed expressions inside string literals.
```python 
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
```
**.format() Method** - The `.format()` method allows you to insert values into a string using placeholders.
```python
name = "Bob"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
```
## String Methods and Operations
### String Indexing and Slicing
Strings in Python are sequences of characters, and you can access individual characters using indexing. Slicing allows you to extract a substring from a string.
```python 
text = "Hello, World!"
print(text[0])  # H
print(text[7:12])  # World
```
### Common String Methods
Python provides several built-in methods to manipulate strings:

- `.upper()`: Converts all characters to uppercase.
    ```python 
    text = "hello"
    print(text.upper())  # HELLO
    ```
- `.lower():` Converts all characters to lowercase.
    ```python 
    text = "HELLO"
    print(text.lower())  # hello
    ```
- `.replace()`: Replaces a substring with another substring.
    ```python
    text = "Hello, World!"
    print(text.replace("World", "Python"))  # Hello, Python!
    ```
- `.split()`: Splits the string into a list of substrings based on a delimiter.
    ```python 
    text = "Hello, World!"
    print(text.split(", "))  # ['Hello', 'World!']
    ```
### Concatenation and Replication of Strings
You can concatenate strings using the `+` operator and replicate them using the `*` operator.
- **Concatenation**:
    ```python 
    text1 = "Hello"
    text2 = "World"
    print(text1 + " " + text2)  # Hello World
    ```
- **Replication**:
    ```python 
    text = "Hello"
    print(text * 3)  # HelloHelloHello
    ```

