# Module 6: Functions

## Goal and Objectives

### Goal
The goal of this module is to introduce you to functions in Python. By the end of this module, you will be able to define, call, and use functions to organize and reuse code effectively.

### Objectives
- Understand what a function is and why it is useful.
- Learn how to define functions using `def`.
- Explore function arguments and return values.
- Differentiate between local and global scope.
- Learn how to call built-in and user-defined functions.
- Understand how to use multiple arguments and default arguments in functions.

## Defining Functions

### What is a Function?
A function is a block of organized, reusable code that performs a single action. Functions provide better modularity and a high degree of code reusability.

### Creating Functions Using `def`
Functions in Python are defined using the `def` keyword.

```python
def greet():
    print("Hello, World!")
```
### Function Arguments and Return Values
Functions can take arguments and return values.
- Arguments
```python 
def greet(name):
    print(f"Hello, {name}!")
```
- Return Values
```python 
    def add(a, b):
        return a + b
    result = add(3, 5)  # 8
```
### Local and Global Scope 
Variables defined inside a function are in the local scope, while variables defined outside are in the global scope.
- Local Scope 
```python 
def my_function():
    x = 10  # Local variable
    print(x)
my_function()
print(x)  # Error: x is not defined
```
- Global Scope
```python 
x = 10  # Global variable
def my_function():
    print(x)
my_function()
print(x)
```
## Calling Functions 
### Calling Built-in Functions 
Python provides many built-in functions that you can call directly.
```python 
print(len("Hello"))  # 5
print(max(1, 2, 3))  # 3
```
### Writing and Calling User-defined Functions
You can write your own functions and call them as needed.
```python 
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
```
### Functions with Multiple Arguments and Default Arguments
Functions can take multiple arguments and have default values for some arguments.
- Multiple Arguments
```python 
def add(a, b):
    return a + b
print(add(3, 5))  # 8
```
- Default Arguments
```python 
def greet(name, message="Hello"):
    print(f"{message}, {name}!")
greet("Alice")  # Hello, Alice!
greet("Bob", "Hi")  # Hi, Bob!
```