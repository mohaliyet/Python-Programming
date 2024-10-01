# Module 9: File Handling

## Goal and Objectives

### Goal
The goal of this module is to introduce you to file handling in Python. By the end of this module, you will be able to open, read, write, and close files, as well as handle file-related errors.

### Objectives
- Learn how to open and close files using `open()` and `with` statements.
- Understand how to read from files using `.read()`, `.readline()`, and `.readlines()`.
- Learn how to write to files using `.write()` and `.writelines()`.
- Handle file-related errors gracefully.

## Working with Files

### Opening and Closing Files
Files can be opened using the `open()` function and closed using the `.close()` method. However, it is recommended to use the `with` statement for better resource management.

- **Opening and Closing Files**
    ```python
    file = open("example.txt", "r")
    content = file.read()
    file.close()
    ```

- **Using `with` Statement**
    ```python
    with open("example.txt", "r") as file:
        content = file.read()
    # No need to explicitly close the file
    ```

### Reading from Files
Python provides several methods to read from files.

- **Reading Entire File with `.read()`**
    ```python
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
    ```

- **Reading Line by Line with `.readline()`**
    ```python
    with open("example.txt", "r") as file:
        line = file.readline()
        while line:
            print(line, end="")
            line = file.readline()
    ```

- **Reading All Lines into a List with `.readlines()`**
    ```python
    with open("example.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line, end="")
    ```

### Writing to Files
Python provides methods to write to files.

- **Writing a Single String with `.write()`**
    ```python
    with open("example.txt", "w") as file:
        file.write("Hello, World!\n")
    ```

- **Writing Multiple Lines with `.writelines()`**
    ```python
    lines = ["First line\n", "Second line\n", "Third line\n"]
    with open("example.txt", "w") as file:
        file.writelines(lines)
    ```

### Handling File-Related Errors
It is important to handle errors that may occur during file operations.

- **Handling FileNotFoundError**
    ```python
    try:
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found")
    ```

- **Handling IOError**
    ```python
    try:
        with open("example.txt", "r") as file:
            content = file.read()
    except IOError:
        print("An I/O error occurred")
    ```

By understanding and applying these file handling techniques, you can effectively manage file operations in your Python programs.