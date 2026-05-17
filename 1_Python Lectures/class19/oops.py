# class Car:
#     # This is an attribute (Class Variable) common to all cars
#     vehType = "Car"
#     # This is a special method called a Constructor.
#     # It runs when you create a new Car object.
#     # init is constructor
#     # class object we need constructor
#     def __init__(self, wheels, make, model, color):
#         self.wheels = wheels
#         self.make = make      # Instance attribute
#         self.model = model    # Instance attribute
#         self.color = color    # Instance attribute
#     # This is a Method (an action the car can do)
#     def move(self, txt="The"):
#         print(f"{txt} {self.vehType} is driving.")

# my_car = Car(4, "Toyota", "Camry", "blue")
# your_car = Car(4, "Honda", "Civic", "red")

# print(f'My {my_car.vehType} is a {my_car.color} {my_car.make} {my_car.model}.')
# print(f"Your {your_car.vehType} has {your_car.wheels} wheels.")

# # 5 attributes and 1 method move

# my_car.move("My")
# your_car.move("Your")

# info = f'My {my_car.wheels} wheeler, {my_car.color} {my_car.make} {my_car.model}'
# print(info, my_car.vehType)


# Encapsulation


class Car:
    __vehType = "Car"

    def __init__(self, wheels, make, model, color):
        self.__wheels = wheels
        self.__make = make      # Instance attribute
        self.__model = model    # Instance attribute
        self.color = color    # Instance attribute

    # This is a Method (an action the car can do)
    def move(self, txt="The"):
        print(f"{txt} {self.__vehType} is driving.")

my_car = Car(4, "Toyota", "Camry", "blue")

print(f'My is a {my_car.color}.')
print(f'My {my_car.vehType} is a {my_car.color} {my_car.make} {my_car.model}.')