lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 43, 56, 34, 43]

# for i in range(1, 11):
#     if i%2==0:
#         # print(i)

e_lst = []
o_lst = []

# for i in lst:
#     if i%2==0:
#         e_lst.append(i)
# print(e_lst)


# for i in lst:
#     if i%2==0:
#         e_lst.append(i)
#     else:
#         o_lst.append(i)

# print(e_lst)
# print(o_lst)

# lst_unique = []

# for i in lst:
#     if i not in lst_unique and lst[i] % 2 == 0:
#         lst_unique.append(i)

# print(lst_unique)

# print(4 * '#')

# for i in range(5):
#     print(5*"#")

# for i in range(1, 6):
#     print(i*"#")

# for i in range(5, 0, -1):
#     print(i*"#")

# for i in range(1, 6, 1):
#     print(i*"# ")
# for i in range(6, 1, -1):
#     print(i*"# ")

# n = 6
# for i in range(1, n, 1):
#     print((n-i) * " " + "#") 

# # pyramid
# n = 6
# for i in range(1, n, 1):
#     print((n-i) * " " + i * "#", end="\b") 
#     print((i) * "#")

# n = 6
# for i in range(1, n, 1):
#     print((n-i) * " " + i * "#", end="") 
#     print((i-1) * "#")

# Diamond
n = 6
for i in range(1, n+1):
    print((n-i) * " " + i * "#", end="\b") 
    print((i) * "#")

for i in range(n-1, 0, -1):
    print((n-i) * " " + (i) * "#", end="\b")
    print((i)*"#")