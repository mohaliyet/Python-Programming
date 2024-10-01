# Module 10: Final Project and Course Review

## Goal and Objectives

### Goal
The goal of this module is to consolidate all the concepts learned throughout the course by designing and implementing a small Python project. Additionally, this module will provide a review of key concepts and introduce intermediate topics for future learning.

### Objectives
- Design and implement a small Python project.
- Review key concepts learned in the course.
- Get introduced to intermediate Python topics for further learning.

## Project: Simple Python Program

### Project Ideas
Design and implement a small Python project based on all the concepts learned. Here are some example projects:

- **Text-based Calculator**
    - Create a calculator that can perform basic arithmetic operations like addition, subtraction, multiplication, and division.
    - Example:
        ```python
        def add(a, b):
            return a + b

        def subtract(a, b):
            return a - b

        def multiply(a, b):
            return a * b

        def divide(a, b):
            if b == 0:
                return "Cannot divide by zero"
            return a / b

        while True:
            print("Options:")
            print("Enter 'add' to add two numbers")
            print("Enter 'subtract' to subtract two numbers")
            print("Enter 'multiply' to multiply two numbers")
            print("Enter 'divide' to divide two numbers")
            print("Enter 'quit' to end the program")
            user_input = input(": ")

            if user_input == "quit":
                break
            elif user_input in ["add", "subtract", "multiply", "divide"]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if user_input == "add":
                    print(f"The result is: {add(num1, num2)}")
                elif user_input == "subtract":
                    print(f"The result is: {subtract(num1, num2)}")
                elif user_input == "multiply":
                    print(f"The result is: {multiply(num1, num2)}")
                elif user_input == "divide":
                    print(f"The result is: {divide(num1, num2)}")
            else:
                print("Unknown input")
        ```

- **To-do List Manager**
    - Create a program that allows users to add, remove, and view tasks in a to-do list.
    - Example:
        ```python
        todo_list = []

        def add_task(task):
            todo_list.append(task)

        def remove_task(task):
            if task in todo_list:
                todo_list.remove(task)

        def view_tasks():
            for task in todo_list:
                print(task)

        while True:
            print("Options:")
            print("Enter 'add' to add a task")
            print("Enter 'remove' to remove a task")
            print("Enter 'view' to view all tasks")
            print("Enter 'quit' to end the program")
            user_input = input(": ")

            if user_input == "quit":
                break
            elif user_input == "add":
                task = input("Enter the task: ")
                add_task(task)
            elif user_input == "remove":
                task = input("Enter the task to remove: ")
                remove_task(task)
            elif user_input == "view":
                view_tasks()
            else:
                print("Unknown input")
        ```

- **Simple Number-Guessing Game**
    - Create a game where the computer randomly selects a number, and the user has to guess it.
    - Example:
        ```python
        import random

        def guess_number():
            number = random.randint(1, 100)
            attempts = 0
            while True:
                guess = int(input("Guess the number (between 1 and 100): "))
                attempts += 1
                if guess < number:
                    print("Too low!")
                elif guess > number:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break

        guess_number()
        ```

## Review and Next Steps

### Recap of Key Concepts
- Why programming and why python 
- Variables and Data Types
- Input/Output and String Manipulation
- Operators and Expressions
- Control Flow (if statements, loops)
- Functions
- Data Structures (lists, tuples, dictionaries)
- File Handling
- Error Handling and Debugging

For a detailed review of these concepts, refer to the [Python Programming: Beginners Level](README.md) file.

### Introduction to Intermediate Topics
- **Advanced Data Structures**
    - Nested lists and comprehensions
    - Advanced dictionary methods: `get()`, `setdefault()`, `.update()`
    - Sorting lists and tuples with `sorted()`, `key` parameter
    - Using `zip()` for combining lists

- **Advanced Functions and Modules**
    - Default argument values
    - Variable-length arguments: `*args` and `**kwargs`
    - Lambda functions and `map()`, `filter()`, `reduce()`
    - Function decorators (basic introduction)
    - Scope and closures

- **Object-Oriented Programming (OOP)**
    - Introduction to Object-Oriented Programming (OOP)
    - Defining classes and creating objects
    - Class attributes and instance attributes
    - Methods: instance methods, class methods, static methods
    - Inheritance and Polymorphism

- **File Handling and Working with CSV**
    - Working with different file modes: `r`, `w`, `a`, `rb`, `wb`
    - Working with directories: `os` and `shutil` modules
    - Managing file paths using `os.path` and `pathlib`
    - Reading and writing CSV files using the `csv` module
    - Working with CSV files using `pandas` (optional introduction)

- **Working with APIs and JSON Data**
    - What is an API? Introduction to RESTful APIs
    - Making HTTP requests using `requests` module
    - Parsing JSON data: loading, accessing, and modifying JSON
    - Sending data with POST requests

- **Regular Expressions (Regex)**
    - Introduction to Regular Expressions (Regex)
    - Common regex patterns for text matching
    - Using the `re` module: `match()`, `search()`, `findall()`, `sub()`
    - Applications of regex in text processing

- **Working with Databases**
    - Introduction to relational databases
    - Setting up and working with SQLite in Python using `sqlite3`
    - Basic SQL operations: SELECT, INSERT, UPDATE, DELETE
    - Connecting Python to an external database
    - Querying data from the database

- **Introduction to Testing and Debugging**
    - Using Python's `pdb` module for debugging
    - Effective use of print debugging vs using `pdb`
    - Using logging for tracking program execution (`logging` module)
    - Introduction to unit testing
    - Writing tests using `unittest`
    - Writing test cases for functions and classes
    - Running tests and checking results

## Resources

- **Python Documentation**: [https://docs.python.org/3/](https://docs.python.org/3/)