# def my_procedure(a):
#     print(f'Hello {a}: From my procedure!')

# my_procedure("Python")

# y = my_procedure("MAS")
# print(y)

# def addThree(a):
#     b = a + 3
#     return b

# x = addThree(12)
# print(x)

# def Sub(a, b):
#     res = a - b
#     return res

# sub = Sub(3423322, 3422302)
# print(sub)

# def calc(a, b, ops):
#     a = float(input("Enter 1st Number: "))
#     b = float(input("Enter 2nd Number: "))
#     ops = input("Enter an Operator e.g. +, -: ")

#     if ops == "+":
#         c = a + b
#     elif ops == "-":
#         c = a - b
#     elif ops == "*":
#         c = a * b
#     else:
#         c = "N/A"

#     return c

# calculator = calc(12, 21, "+")
# print(calculator)

# def grade(marks):
#     marks = int(input("Enter your marks : "))

#     if 80 <= marks < 100:
#         grade = "A"
#     elif 60 <= marks < 80:
#         grade = "B"
#     elif 50 <= marks < 60:
#         grade = "C"
#     else:
#         grade = "F"
    
#     return print(f"Your grade is {grade}.")

# result = grade(78)

# def grade(marks):
#     marks = int(input("Enter your marks : "))
#     grade = ["A", "B", "C", "F"]

#     if 80 <= marks < 100:
#         g = grade[0]
#     elif 60 <= marks < 80:
#         g = grade[1]
#     elif 50 <= marks < 60:
#         g = grade[2]
#     else:
#         g = grade[3]

#     return print(f"Your grade is {g}.")

# result = grade(78)

def pattern(n, pat_name):
    name = pat_name.lower()
    
    if name == "pyramid":
        for i in range(1, n + 1):
            print(" " * (n - i) + "# " * i)

    elif name == "diamond":
        # Upper half
        for i in range(1, n + 1):
            print(" " * (n - i) + "# " * i)
        # Lower half
        for i in range(n - 1, 0, -1):
            print(" " * (n - i) + "# " * i)
            
    else:
        print("Enter correct value (Pyramid or Diamond)")

pattern(12, "diamond")
