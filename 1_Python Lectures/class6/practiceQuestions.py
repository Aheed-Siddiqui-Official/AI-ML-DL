# ///////////////////////////   Section A => Basics, Strings, and Lists   //////////////////////////////

# # Question 1
# Name = "Aheed"
# Course = "Python"
# Year = 2026

# print(f"Name:{Name} | Course:{Course} | Year:{Year}")

# # Question 2
# Name = "Aheed"
# Course = "Python"
# Year = 2026

# print(f"Name:{Name} | Course:{Course} | Year:{Year}")

# Question 3
# var = 10
# print(var)
# var = 10.5
# print(var)
# var = "Python"
# print(var)

# Question 4
# Number1 = 23
# Number2 = 32
# Sum = Number1 + Number2
# Division = Number1 // Number2
# Remainder = Number1 % Number2

# print(f"Sum = {Sum}, Division = {Division}, Remainder = {Remainder}")

# # Question 5
# birthYear = 2005
# calcAge = 2026-2005

# print(f"Your current age is approx = {calcAge}")

# # Question 6
# a = int(input("Enter number 1 : "))
# b = int(input("Enter number 2 : "))

# a, b = b, a
# print(f"a = {a}, b = {b}")

# Question 7 
# a = int(input("Enter number 1 : "))
# b = int(input("Enter number 2 : "))
# c = 0

# c = a
# a = b
# b = c

# print(f"a = {a}, b = {b}")

# Question 8
# a = 6
# print(a)
# a += a
# print(a)
# a *= a
# print(a)

# Question 9
# lang = "Python"
# code = "Programming"
# express = "Language"

# print(f"{lang}\n {code}\n\t{express}")

# Question 10
# strings = "My name is Aheed"
# print(strings[0], len(strings), strings[-1])

# # Question 11
# slices = "Programming"
# print(slices[0:4])
# print(slices[1:8])

# Question 12
# reverse = "Programming"
# reversed = reverse[::-1]
# print(reversed)

# Question 13
# steps = "Programming in Python"
# length = len(steps)
# final = steps[0:length:2]
# print(final)

# # Question 14
# string1 = "Python"
# string2 = "No Python"

# print(string1 == string2)

# Question 15 
# exist = "Does the word exists?"
# print("Does" in exist)

# Question 16
# string = "converT"

# print(string.upper())
# print(string.lower())
# print(string.title())

# Question 17
# sentence = "I like java"
# replaced = sentence.replace("java", "python")

# print(replaced)

# Question 18
# string = "Big Data Analytics"

# print(string.index("D"))

# Question 19
# sentence = "My name is Muhammad Aheed Siddiqui"

# print(sentence.split())

# Question 20
lists = ["Java", "Python", "JS", "Rust", "Typescript", "Bootstrap"]

# Question 21
print(lists[1], lists[2])

# Question 22
lists.insert(2, "Golang")
print(lists)
lists.append("Cpp")
print(lists)

# Question 23
lists.pop()
print(lists)
lists.remove("Java")
print(lists)

# Question 24
sliced = lists[0:2]
print(sliced)

# Question 25
unsort = [3, 4, 6, 7, 2, 1, 5, 7, 9, 0]
sort = unsort.sort()

print(unsort)