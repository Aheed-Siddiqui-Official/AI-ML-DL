# import module
import module as mx
import datetime

# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))

# print(module.Calc(num1, num2))

# a = module.person1["age"]
# print(a)

# a = mx.person1["age"]
# print(a)

# x = datetime.datetime.now()

# print(x.year)
# print(x.strftime("%A"))

# x = datetime.datetime(202, 5, 17)
# print(x)

# print("Even" if 3 % 2 == 0 else "odd")

n = int(input("Enter : "))

# output = "even" if n % 2 == 0 else "odd" if n % 2 == 1 else None
# print(output)

output = "A" if n >= 80 else "B" if n>= 70 else "C" if n >= 60 else "F"
print(output)