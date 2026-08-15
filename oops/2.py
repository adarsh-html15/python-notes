class Students():
    collage_name= "JASS collage"
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
        print('Adding new student and their marks')
        print(name,mark)

s1 = Students("Adarsh",97)

#Methods


class Students():
    collage_name= "JASS collage"
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    def hello(self):  # Methods are functions that belongs to objects
        print("hellow",self.name)

s1 = Students("Adarsh",97)
s1.hello()    

# Static method = dont use self parameter (work as class level)
#  @staticmethod     decorator    
class Students():
    collage_name= "JASS collage"
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
        print(name,mark)
    @staticmethod
    def  you():
        print("Hellow world❤️")   
s2 = Students("Aakansha",84)
s2.you()        