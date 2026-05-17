# txt = "python"

# for i in txt:
#     if i == i[::-1]:
#         res = "\b"
#     else:
#         res = "NOT"

# print(f"{i} is {res} a Palindrome")

# print("i" " j")
# print("====")

# for i in range(1, 6):
#     for j in range(2, 4):
#         print(i, j)

#     print("----")

#  two tables vertical
# for t in range(2, 4, 1):
#     for m in range(1, 6, 1):
#         print(t, "x", m, "=", t*m)

#     print("----------")

#  two tables horizontal
# for m in range(1, 6, 1):
#     for t in range(2, 4, 1):
#         print(t, "x", m, "=", t*m, end="\t")

#     print("")

lst = [10, 9.4, 12, 2, 3, 4, 2.4, 4, 12, 21]
i = 1

Rating = lst[0]
while(Rating >= 6):
    print(Rating)
    Rating = lst[i]
    i = i+1

