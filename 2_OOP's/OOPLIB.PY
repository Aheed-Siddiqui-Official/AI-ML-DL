from abc import ABC, abstractmethod
class Vehicle(ABC):
# This is a special method called a Constructor.
# It runs when you create a new object.
    def __init__(self, wheels, make, model, color):
        self.__vehType = "Vehicle" # __ Private instance attribute
        self.__wheels = wheels # __ Private instance attribute
        self._make = make # _ Protected instance attribute
        self._model = model # _ Protected instance attribute
        self.color = color # Public instance attribute
    def set_vehType(self, vehType):
        self.__vehType = vehType # A public method to set the private attribute
    def get_vehType(self):
        return self.__vehType # A public method to access the private attribut
    def get_wheels(self):
        return self.__wheels # A public method to access the private attribute
    def get_info(self):
        infor = f"{self.color} {self.__wheels}-wheeler, {self._make} {self._model}"
        return infor
        
    @abstractmethod
    def move(self, txt="The"):
        pass

class Car(Vehicle):
    def __init__(self, wheels, make, model, color):
        super().__init__(wheels, make, model, color)
        self.set_vehType("Car")

    def move(self, txt="The"):
        print(f"{txt} {self.get_vehType()} is being driven.")

class MotorBike(Vehicle):
    def __init__(self, wheels, make, model, color):
        super().__init__(wheels, make, model, color)
        self.set_vehType("Bike")
    def move(self, txt="The"):
        print(f"{txt} {self.get_vehType()} is being ridden.")
