# del to delete 

class Student():
    def __init__(self,name):
        self.name =name
s1 = Student("Adarsh")
print(s1.name)
del s1.name
# print(s1.name)/

class Account():
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_passacc_pass = acc_pass
             # putting 2 underscore __ make the attribute private and can't access
            # we can only access into the class
acc1 = Account("12345","abcde")   
print(acc1.acc_no) 
# print(acc1.acc_pass)    like we can'nt access here

