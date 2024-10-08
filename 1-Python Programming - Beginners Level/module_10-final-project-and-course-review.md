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
    - Create a game where the user thinks of a number between 1 and 100, and the computer tries to guess it based on the user's feedback.
    - Example:
        ```python
        def guess_number():
            low = 1
            high = 100
            attempts = 0
            print("Think of a number between 1 and 100, and I will try to guess it.")
            while True:
                guess = (low + high) // 2
                attempts += 1
                print(f"My guess is: {guess}")
                feedback = input("Is it too high (H), too low (L), or correct (C)? ").upper()
                if feedback == "H":
                    high = guess - 1
                elif feedback == "L":
                    low = guess + 1
                elif feedback == "C":
                    print(f"Congratulations! I guessed the number in {attempts} attempts.")
                    break
                else:
                    print("Invalid input. Please enter H, L, or C.")
        
        guess_number()
        ```

## Review and Next Steps

### Recap of Key Concepts
- **Why programming and why python**
- **Variables and Data Types**
- **Input/Output and String Manipulation**
- **Operators and Expressions**
- **Control Flow (if statements, loops)**
- **Functions**
- **Data Structures (lists, tuples, dictionaries)**
- **Error Handling and Debugging**
- **File Handling**

For a detailed review of these concepts, refer to the [Python Programming: Beginners Level](README.md) file.

### Introduction to Intermediate Topics
- **Advanced Data Structures**
- **Advanced Functions and Modules**
- **Object-Oriented Programming (OOP)**
- **Advanced Error Handling and Exceptions**
- **File Handling and Working with CSV**
- **Working with APIs and JSON Data**
- **Regular Expressions (Regex)**
- **Working with Databases**
- **Introduction to Testing and Debugging**
## Resources

- **Python Documentation**: [https://docs.python.org/3/](https://docs.python.org/3/)