# Abstraction
# HIding the implimentation details of a class
class Car():
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = True
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started....")
car1 = Car()
car1.start() # implimentation details are hide

# Encaptulation
# Wrapping data and functions into a sinlge unit(object)

# Objects are like capsules