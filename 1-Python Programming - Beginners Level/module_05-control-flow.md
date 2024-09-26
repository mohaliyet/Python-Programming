# Module 5: Control Flow

## Goal and Objectives

### Goal
The goal of this module is to introduce you to control flow mechanisms in Python. By the end of this module, you will be able to use conditional statements and loops to control the execution flow of your programs.

### Objectives
- Learn about conditional statements and how to use them.
- Understand how to use loops to repeat actions.
- Explore loop control statements.

## Conditional Statements

### The `if`, `else`, `elif` Structure
Conditional statements allow you to execute certain blocks of code based on conditions.

- `if` statement
    ```python
    x = 10
    if x > 5:
        print("x is greater than 5")
    ```
- `else` statement
    ```python
    x = 3
    if x > 5:
        print("x is greater than 5")
    else:
        print("x is not greater than 5")
    ```
- `elif` statement
    ```python
    x = 5
    if x > 5:
        print("x is greater than 5")
    elif x == 5:
        print("x is equal to 5")
    else:
        print("x is less than 5")
    ```

### Nested Conditions
You can nest conditions inside other conditions.

```python
x = 10
y = 20
if x > 5:
    if y > 15:
        print("x is greater than 5 and y is greater than 15")
```

### Boolean Logic in Control Flow
Boolean logic can be used to combine multiple conditions.

```python 
x = 10
y = 20
if x > 5 and y > 15:
    print("x is greater than 5 and y is greater than 15")
```
## Loops
### `while` Loops
`while` loops repeat a block of code as long as a condition is true.

```python 
i = 1
while i < 5:
    print(i)
    i += 1
```
### `for` Loops
`for` loops iterate over a sequence of elements.
```python 
for i in range(5):
    print(i)
```
### Loop Control Statements
Control the flow of loops using `break` and `continue`.
- `break`: Exit hte loop
```python 
for i in range(5):
    if i == 3:
        break
    print(i)
```
- `continue`: Skip the current iteration and continue with the next
```python 
for i in range(5):
    if i == 3:
        continue
    print(i)
```
### `range()` Function for Loops
The `range()` function generates a sequence of numbers, which is useful for looping a specific number of times.

```python 
for i in range(1, 10, 2):
    print(i)  # Prints 1, 3, 5, 7, 9
```