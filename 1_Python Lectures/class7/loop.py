lst = [1, 2, 3, 4, 5, 3, 4, 5, 2, 3, 6, 8, 6, 8, 9, 2, 4, 5, 10, 3]

# print("[", end="")

# for i in lst:
#     print(f"{i}", end=", ")

# print("\b\b]")
# Expected output => [1, 2, 3, 4, 5, 3, 4, 5]

# sum = 0
# for i in lst:
#     sum += lst[i]
#     print(i)

# print(f"==\n",sum)

# sum = 0
# for i in lst:

#     if lst[i] % 2 == 0:
#         sum += lst[i]
#     else:
#         pass

# print("Even sum = ", sum)

# min = lst[0]
# for i in lst:
#     if min > lst[i+1]:
#         min = i

# print("Minimum number = ", min)

# max = lst[0]
# for i in lst:
#     if max < lst[i+1]:
#         max = i

# print("Max number = ", max)

count = 0
# for i in lst:
#     count += 1

# print(count)

sum = 0
for i in lst:

        sum += lst[i]
        count += 1

avg = sum/count
print(avg)