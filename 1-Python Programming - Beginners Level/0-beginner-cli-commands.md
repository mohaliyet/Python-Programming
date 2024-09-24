# CMD and Terminal Commands Cheat Sheet

## Understanding GUI vs CLI

- **GUI (Graphical User Interface)**: A user-friendly interface that allows users to interact with electronic devices using graphical icons and visual indicators.
- **CLI (Command Line Interface)**: A text-based interface used to interact with software and operating systems by typing commands into a console or terminal.

## Understanding CMD vs Terminal

- **CMD (Command Prompt)**: A command line interpreter application available in most Windows operating systems. It allows users to execute commands to perform various tasks.
- **Terminal**: A command line interface used in Unix-based systems (like Linux and macOS) to interact with the operating system by executing commands.

## Beginner Level Commands

| Command                       | Description                                                                 | CMD  | Terminal |
| ----------------------------- | --------------------------------------------------------------------------- | ---- | -------- |
| `pwd`                         | Print the current working directory.                                        |      | ✔️       |
| `ls`                          | List files and directories in the current directory.                        |      | ✔️       |
| `dir`                         | List files and directories in the current directory.                        | ✔️   |          |
| `cd <directory>`              | Change the current directory to `<directory>`.                              | ✔️   | ✔️       |
| `cd ..`                       | Move up one directory level.                                                | ✔️   | ✔️       |
| `cd ~`                        | Change to the home directory.                                               |      | ✔️       |
| `cd %HOMEPATH%`               | Change to the home directory.                                               | ✔️   |          |
| `mkdir <directory>`           | Create a new directory named `<directory>`.                                 | ✔️   | ✔️       |
| `rmdir <directory>`           | Remove an empty directory named `<directory>`.                              | ✔️   | ✔️       |
| `rm <file>`                   | Remove a file named `<file>`.                                               |      | ✔️       |
| `del <file>`                  | Remove a file named `<file>`.                                               | ✔️   |          |
| `cp <source> <destination>`   | Copy a file or directory from `<source>` to `<destination>`.                |      | ✔️       |
| `copy <source> <destination>` | Copy a file or directory from `<source>` to `<destination>`.                | ✔️   |          |
| `mv <source> <destination>`   | Move or rename a file or directory from `<source>` to `<destination>`.      |      | ✔️       |
| `move <source> <destination>` | Move or rename a file or directory from `<source>` to `<destination>`.      | ✔️   |          |
| `touch <file>`                | Create a new empty file named `<file>`.                                     |      | ✔️       |
| `echo. > <file>`              | Create a new empty file named `<file>` (Windows equivalent of `touch`).     | ✔️   |          |
| `type nul > <file>`           | Create a new empty file named `<file>` (another Windows equivalent of `touch`). | ✔️   |          |
| `echo <text> > <file>`        | Write `<text>` to `<file>`, creating the file if it doesn't exist.          | ✔️   | ✔️       |
| `echo <text> >> <file>`       | Append `<text>` to `<file>`.                                                | ✔️   | ✔️       |
| `cat <file>`                  | Display the contents of a file.                                             |      | ✔️       |
| `type <file>`                 | Display the contents of a file.                                             | ✔️   |          |
| `clear`                       | Clear the terminal screen.                                                  |      | ✔️       |
| `cls`                         | Clear the CMD screen.                                                       | ✔️   |          |