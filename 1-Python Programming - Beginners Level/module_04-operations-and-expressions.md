# Module 4: Operators and Expressions

## Goal and Objectives

### Goal

The goal of this module is to introduce you to operators and expressions in Python. By the end of this module, you will be able to use various operators to perform calculations and evaluate expressions.

### Objectives

- Learn about different types of operators in Python.
- Understand how to evaluate expressions.
- Explore the precedence of operators.

## Operators in Python

### Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

- `+`: Addition
  ```python
  result = 3 + 2  # 5
  ```
- `-`: Subtraction
  ```python
  result = 3 - 2  # 1
  ```
- `*`: Multiplication
  ```python
  result = 3 * 2  # 6
  ```
- `/`: Division
  ```python
  result = 3 / 2  # 1.5
  ```
- `%`: Modulus
  ```python
  result = 3 % 2  # 1
  ```
- `**`: Exponentiation
  ```python
  result = 3 ** 2  # 9
  ```
- `//`: Floor Division
  ```python
  result = 3 // 2  # 1
  ```

### Comparison Operators

Comparison operators are used to compare two values.

- `==`: Equal to
  ```python
  result = (3 == 2)  # False
  ```
- `!=`: Not equal to
  ```python
  result = (3 != 2)  # True
  ```
- `>`: Greater than
  ```python
  result = (3 > 2)  # True
  ```
- `<`: Less than
  ```python
  result = (3 < 2)  # False
  ```
- `>=`: Greater than or equal to
  ```python
  result = (3 >= 2)  # True
  ```
- `<=`: Less than or equal to
  ```python
  result = (3 <= 2)  # False
  ```

### Logical Operators

Logical operators are used to combine conditional statements.

- `and`: Returns True if both statements are true
  ```python
  result = (3 > 2 and 2 > 1)  # True
  ```
- `or`: Returns True if one of the statements is true
  ```python
  result = (3 > 2 or 2 < 1)  # True
  ```
- `not`: Reverses the result, returns False if the result is true
  ```python
  result = not(3 > 2)  # False
  ```

### Assignment Operators

Assignment operators are used to assign values to variables.

- `=`: Assign
  ```python
  x = 5
  ```
- `+=`: Add and assign
  ```python
  x += 3  # x = x + 3
  ```
- `-=`: Subtract and assign
  ```python
  x -= 3  # x = x - 3
  ```
- `*=`: Multiply and assign
  ```python
  x *= 3  # x = x * 3
  ```
- `/=`: Divide and assign
  ```python
  x /= 3  # x = x / 3
  ```

## Expressions and Order of Operations

### Evaluating Expressions

Expressions are combinations of values and operators that can be evaluated to produce a result.

```python
result = (3 + 2) * 2  # 10
```

### Precedence of Operators

Operator precedence determines the order in which operations are performed in an expression.

- Parentheses `()`
- Exponentiation `**`
- Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%`
- Addition `+`, Subtraction `-`

  ```python
  result = 3 + 2 * 2  # 7 (Multiplication before Addition)
  result = (3 + 2) * 2  # 10 (Parentheses first)
  ```
