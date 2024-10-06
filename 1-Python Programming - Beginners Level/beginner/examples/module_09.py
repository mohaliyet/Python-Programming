try:
	with open('example_not_exist.txt','r',encoding='utf-16') as file:
		content = file.write('hellow, world')
except FileNotFoundError:
	print('the file you are referring is not in the directory!')
except IOError:
	print('you cannot write to this file as it is read-only!')