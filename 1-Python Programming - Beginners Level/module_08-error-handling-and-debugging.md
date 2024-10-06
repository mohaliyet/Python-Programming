# Module 8: Error Handling and Debugging

## Goal and Objectives

### Goal
The goal of this module is to introduce you to error handling and debugging in Python. By the end of this module, you will be able to identify and handle different types of errors, use exception handling to write robust programs, and debug your code effectively.

### Objectives
- Understand different types of errors in Python.
- Learn how to handle exceptions using `try`, `except`, and `finally` blocks.
- Learn how to raise exceptions using `raise`.
- Understand how to write robust programs using exception handling.
- Learn basic debugging techniques.

## Understanding Errors in Python

### Types of Errors
Errors in Python can be broadly classified into two categories: syntax errors and runtime errors.

- **Syntax Errors**: These occur when the parser detects an incorrect statement.
    ```python
    print("Hello, World!  # SyntaxError: EOL while scanning string literal
    ```

- **Runtime Errors**: These occur during the execution of a program.
    ```python
    print(10 / 0)  # ZeroDivisionError: division by zero
    ```

### Common Python Errors
Here are some common Python errors you might encounter:

- **TypeError**: Raised when an operation or function is applied to an object of inappropriate type.
    ```python
    print("2" + 2)  # TypeError: can only concatenate str (not "int") to str
    ```

- **ValueError**: Raised when a function receives an argument of the right type but inappropriate value.
    ```python
    int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'
    ```

- **IndexError**: Raised when a sequence subscript is out of range.
    ```python
    lst = [1, 2, 3]
    print(lst[3])  # IndexError: list index out of range
    ```

- **KeyError**: Raised when a dictionary key is not found.
    ```python
    d = {"name": "Alice"}
    print(d["age"])  # KeyError: 'age'
    ```

## Basic Exception Handling

### Using `try`, `except`, `finally` Blocks
Exception handling in Python is done using `try`, `except`, and `finally` blocks.

- **Basic `try` and `except`**
    ```python
    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    ```

- **Catching Multiple Exceptions**
    ```python
    try:
        print(10 / 0)
    except (ZeroDivisionError, TypeError) as e:
        print(f"An error occurred: {e}")
    ```

- **Using `finally`**
    ```python
    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("This will always execute")
    ```

### Raising Exceptions Using `raise`
You can raise exceptions using the `raise` keyword.

- **Raising an Exception**
    ```python
    def check_positive(number):
        if number < 0:
            raise ValueError("Number must be positive")
        return number

    try:
        check_positive(-1)
    except ValueError as e:
        print(e)  # Number must be positive
    ```

## Writing Robust Programs Using Exception Handling
Exception handling allows you to write programs that can handle unexpected situations gracefully.

- **Example: Handling File Operations**
    ```python
    try:
        with open("file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
   
        print("File not found.")
    ```

## Basic Debugging Techniques

### Using Print Statements
One of the simplest ways to debug your code is by using print statements to track the flow of execution and the values of variables.

- **Example**
    ```python
    def add(a, b):
        print(f"a: {a}, b: {b}")  # Debugging print statement
        return a + b

    result = add(2, 3)
    print(f"Result: {result}")
    ```

### Using a Debugger
Most modern IDEs, including Visual Studio Code, come with built-in debuggers that allow you to set breakpoints, step through code, and inspect variables.

- **Setting Breakpoints and Stepping Through Code**
    - Open your Python file in Visual Studio Code.
    - Click in the gutter next to the line number where you want to set a breakpoint.
    - Start debugging by clicking on the debug icon or pressing `F5`.
    - Use the debug controls to step through your code and inspect variables.

By understanding and applying these error handling and debugging techniques, you can write more robust and maintainable Python programs.