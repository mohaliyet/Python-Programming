# matrix = [[1, 2, 3], 
#           [4, 5, 6], 
#           [7, 8, 9]]

# print(matrix[0][2])

# sqr = []

# for i in range(11):
#     sqr.append(i**2)

# sqr = [i**2 for i in range(11)]

# print(sqr)

# nested_list = [[1, 2, 3],
#                [4, 5, 6], 
#                [7, 8, 9]]

# flattened_list = [i for 
#                   row in 
#                   nested_list 
#                   for i in row] 
# print(flattened_list) 

even_sqr = [i**2 
            for i in range(11) 
            if i % 2 == 0]
print(even_sqr)

