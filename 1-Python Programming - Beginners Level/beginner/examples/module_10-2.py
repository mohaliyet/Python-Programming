def add_task(task):
	todo_list.append(task)
def remove_task(task):
	if task in todo_list:
		todo_list.remove(task)
def view_tasks():
	print("\nYour tasks in the todo list are: ")
	for task in todo_list:
		print(task)
def save_task(filename, todolists):
	with open(filename, 'w', encoding='utf-16') as tasks:
		for todolist in todolists:
			tasks.write(todolist+'\n')
def read_task(filename):
	with open(filename,'r',encoding='utf-16') as tasks:
		print("\nYour tasks in the todo list file are: ")
		lines = tasks.readlines()
		for line in lines:
			print(line,end="")


todo_list = []

while True:
	print("\nOptions:")
	print("Enter 'add' to add a task")
	print("Enter 'remove' to remove a task")
	print("Enter 'view' to view all the tasks")
	print("Enter 'save' to save a todo list into a file")
	print("Enter 'read' to read a todo list from a file")
	print("Enter 'quit' to end the program")
	user_input = input(": ")
	
	try:
		if user_input == "quit":
			break
		elif user_input == "add":
			task = input("Enter the task: ")
			add_task(task)
		elif user_input == "remove":
			task=input("Enter the task to remove: ")
			remove_task(task)
		elif user_input == "save":
			filename=input("Enter the filename: ")
			save_task(filename,todo_list)
		elif user_input == "read":
			filename=input("Enter the filename: ")
			read_task(filename)
		elif user_input == "view":
			view_tasks()
		else:
			print("\nUnknown input! Please try again!")
	except FileNotFoundError:
		print('There is no such file in the directory!')
	
		









