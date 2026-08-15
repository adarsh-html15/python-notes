# Inheritance
# DERIVES A CLASS PROPERTY INTO ANOTHER CLASS

class Car():
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stoped")


class Toyotacar(Car):
    def __init__(self,name):
        self.name = name

car1 = Toyotacar("fortuner")
car2 = Toyotacar("prius")

print(car1.start())
print(car2.start())

# super method
class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()

# class method
class Parent:
    @classmethod
    def identify(cls):
        # cls dynamically evaluates to the calling class
        return f"This is the {cls.__name__} class."

class Child(Parent):
    pass

# Calling the class method
print(Parent.identify())  # Output: This is the Parent class.
print(Child.identify())   # Output: This is the Child class. 

   


        
