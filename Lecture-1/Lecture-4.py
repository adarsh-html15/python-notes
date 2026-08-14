# dictionary
# store with key valuse , unorderd , mutable , can't dublecate key
dict = {
    "name":"Adarsh",
    "age":21,
    "height":5.10
    }
print(dict)
print(type(dict))

print(dict["name"])
dict["age"] = 23

nul_dict = {}

# Nested distionary

dict2 = {
    "name":"Adarsh",
    "age":21,
    "height":5.10,
    "Subject":{
        "python":79,
        "javascript":93,
        "html":97
    }
    }

# dict method
"""
    list.keys()
    list.valuse()
    dict.items()
    dict.get("key")
    dict.update(newDict)
                        """
# SET 
# collections of unorderd items , set mutable(but element immutable), unique
num = {2,3,4,5,6,"Adarsh"}
#for empty set
collection = set() #empty
#Set method    
num.remove(2)
num.clear()#to empty set
num.add(10)
# num.pop() random
print(num)

# method
"""
    set.union(set2)
    set.intersection(set2)
                            """

