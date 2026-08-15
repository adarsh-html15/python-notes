# Class = Blueprint of objects
class Student:
    name="Adarsh"

# Object (instance)
    
s1 = Student()
print(s1.name)    


class Car:
    color="blue"
    brand="gls"

s2 = Car()
print(s2.color)
print(s2.brand)


# Constructor
'''all the classes have fun called __init__() , which is alwyas executed when the object is being called'''

class Student:
    name="Adarsh"
    def __init__(self , fullname,marks): #self is student object
        self.name = fullname
        self.marks= marks
        print("Add new student to the class")
        print(self.name)
        print(self.marks)

s3 = Student("Aakansha",55)
# print(s3.name)




