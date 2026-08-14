#Loops
#while loops
count = 1
while count <=5:
    print("hellow")
    count +=1
print(count)

while count <=20:
    print(count)
    count +=1
# Break(break) & Continue(skip)
i = 1
while i<10:
    if(i==5):
        print("the num is five")
        i+=1
        # break
    else:
        print("finding...")
        i+=1
        
#for loop
# for sequential loop        
list = [1,2,3,4,5,6,7]
for val in list:
    print(val)        
else:           #we can use else in loops
    print("END")
    
tup = (1,2,3,4,5,6,7,8,9)
for val in tup:
    print(val)
    if(val==8):
        print(val," is awalble in the tuuple.")
else:
    print("end")         
    
    
# Range
    """" (start,skip,step)"""
#for el in range(1,5,3)
#   print(el) 

# pass    to pass a nul statment