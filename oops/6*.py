# polymorphism
#when the same operater is allowed to have meaning according to the context

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i+",self.img,"j")

#dunder function "" __add__,__sub__,__mul__""
    def __add__(self,num2):
        newReal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newReal,newimg)
            
num1 = Complex(1,3)
num1.showNumber()        
num2 = Complex(3,8)
num2.showNumber()
num3 = num1 + num2
print("-----------")
num3.showNumber()


