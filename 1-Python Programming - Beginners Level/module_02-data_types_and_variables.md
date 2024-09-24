# Module 2: Data Types and Variables

## Goal and Objectives

### Goal
The goal of this module is to introduce you to the fundamental `data types` in Python and how to work with `variables`. By the end of this module, you will understand different `data types`, how to `create and use variables`, and perform `basic operations` with them.

### Objectives
- Understand the different data types in Python.
- Learn how to create and use variables.
- Understand naming conventions for variables.
- Learn about constants and their usage.
- Perform basic operations with variables.
- Understand type conversion in Python.

## Data Types

### Numbers
Python supports different types of numbers, including integers and floats.

- **Integers**: Whole numbers without a decimal point.
    ```python
    x = 5
    y = -3
    ```
- **Floats:** Numbers with a decimal point.
    ```python
    a = 3.14
    b = -2.5
    ```
### Strings
Strings are sequences of characters enclosed in quotes.

- **Single-line strings:** Enclosed in single or double quotes.
    ```python
    name = "Alice"
    greeting = 'Hello, World!'
    ```
- **Multi-line strings:** Enclosed in triple quotes.
    ```python
    message = """This is a
    multi-line string."""
    ```
### Booleans
Booleans represent one of two values: `True` or `False`.

    ```python 
    is_active = True
    is_logged_in = False
    ```
### Type conversion
Python provides built-in functions to convert between different data types.
- Convert to integer: `int()`
    ```python 
    num_str = "10"
    num_int = int(num_str)  # Converts string to integer
    ```
- Convert to float: `float()`
    ```python
    num_str = "10.5"
    num_float = float(num_str)  # Converts string to float
    ```
- Convert to string: `str()`
    ```python
    num = 10
    num_str = str(num)  # Converts integer to string
    ```

## Variables
### Creating Variables and Naming Conventions
Variables are used to store data that can be referenced and manipulated in a program.

- **Creating variables:**
    ```python
    age = 25
    name = "Bob"
    ```
- **Naming conventions:**
    - Variable names should be descriptive and meaningful.
    - Use lowercase letters and underscores to separate words (snake_case).
    - Variable names must start with a letter or an underscore (_), but not with a number.
    - Variable names can contain letters, numbers, and underscores, but no special characters (e.g., @, #, $, etc.).
    - Variable names are case-sensitive (e.g., `age` and `Age` are different variables).
    - Avoid using reserved keywords and special characters. 
        ```python
        False      await      else       import     pass
        None       break      except     in         raise
        True       class      finally    is         return
        and        continue   for        lambda     try
        as         def        from       nonlocal   while
        assert     del        global     not        with
        async      elif       if         or         yield
        ```
    ```python
    first_name = "John"
    last_name = "Doe"
    ```
### Constants and Their Usage
Constants are variables whose values should not change throughout the program. By convention, constants are written in uppercase letters with underscores separating words.

    ```python
    PI = 3.14159 
    MAX_USERS = 100
    ```
### Basic Operations with Variables
You can perform various operations with variables, such as arithmetic operations, string concatenation, and boolean operations.
- **Arithmetic operations:**
    ```python
    x = 10
    y = 5
    sum = x + y  # Addition
    difference = x - y  # Subtraction
    product = x * y  # Multiplication
    quotient = x / y  # Division
    ```
- **String concatenation:**
    ```python
    first_name = "Jane"
    last_name = "Smith"
    full_name = first_name + " " + last_name  # Concatenates strings
    ```
- **Boolean operations**
    ```python
    is_sunny = True
    is_rainy = False
    is_good_weather = is_sunny and not is_rainy  # Logical AND and NOT
    ```