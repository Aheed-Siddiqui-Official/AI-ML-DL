# functionality is called objects
# features and properties is called classes

import enum

# class Day(enum.Enum):
#     Sunday = 1
#     Monday = 2
#     Tuesday = 3

# print(Day["Sunday"].value)

# class Name():
#     a = "MAS"
#     b = "AAS"

# print(Name.a)

# n1 = Name.a
# n2 = Name.b

# print(n1)
# print(n2)

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print("Hello, my name is " + self.name)


# p1 = Person("john", 32)
# p1.greet()

# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(self.name + " Says woof!")

# d1 = Dog("Caramel", 2)
# d1.bark()

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

# car1 = Car("Toyota", "Corolla")

# print(car1.brand)
# print(car1.model)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Linus", 30)

# del p1.age
# print(p1.name)
# print(p1.age) # This would cause an error

# class Person:
#     lastname = ""

#     def __init__(self, name):
#         self.name = name

# p1 = Person("Linus")
# p2 = Person("Email")

# Person.lastname= "Refsnes"

# print(p1.lastname)
# print(p2.lastname)

# class Person:
#   def __init__(self, name):
#     self.name = name

# p1 = Person("Tobias")

# p1.age = 25
# p1.city = "Oslo"

# print(p1.name)
# print(p1.age)
# print(p1.city)

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def __str__(self):
#         return f"Student(name = {self.name}, grade = {self.grade})"

# s1 = Student("Anna", "A")
# print(s1)

# s1 = Student("Anna", "B")
# print(s1)

# class Calculator:
#     def add(self, a, b):
#         return a + b
    
#     def mul(self, a, b):
#         return a * b
    
# calc = Calculator()
# print(calc.add(2, 4))
# print(calc.mul(3, 6))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())