# output_list = [i**2 for i in range(5)]
# output_list = [i+1 for i in range(5)]

input_list = [1, 2, 3, 4, 3, 1, 2, 4]
output_list = {i:i**4 for i in input_list}

# print("Output list: ", output_list)
# print("Output dictionary: ", output_list)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

output_matrix = []
for i in matrix:
    for j in i:
        output_matrix.append(j)


print(output_matrix)