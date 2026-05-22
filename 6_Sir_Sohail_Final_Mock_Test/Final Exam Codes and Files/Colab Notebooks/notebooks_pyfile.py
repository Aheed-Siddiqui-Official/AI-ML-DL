from abc import ABC, abstractmethod
class Vehicle(ABC):
  
  def __init__(self, wheels, make, model, color):
    self.__vehType = "Vehicle"
    self.__wheels = wheels    # Private Instance
    self._make = make        # Protected Instance
    self._model = model      # Protectd Instance
    self.color = color        # Public Instance

  def set_vehType(self, vehType): # setter are usually "procedures"
    self.__vehType = vehType

  def get_vehType(self):
    return self.__vehType

  def get_wheels(self):
    return self.__wheels
  def get_info(self):
    return f"Wheels : {self.__wheels}, Make : {self._make}, Model : {self._model}, Color : {self.color}"
  
  @abstractmethod  
  def move(self, txt="The"):
    pass


#------------------------------

class Car(Vehicle):
  def __init__(self, wheels, make, model, color):
    super().__init__(wheels, make, model, color)
    self.set_vehType("Car")
  def move(self, txt="The"):
    print(f"{txt} {self.get_vehType()} is being driven.")

class Motorcycle(Vehicle):
  def __init__(self, wheels, make, model, color):
    super().__init__(wheels, make, model, color)
    self.set_vehType("Motorcycle")

  def move(self, txt="The"):
    print(f"{txt} {self.get_vehType()} is being ridden.")



