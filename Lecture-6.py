# Function (Block of statement)

def sum(a,b):
    s = a+b
    print("sum",s)
    return sum
    
sum(4,6)    

def print_hello():
    print("I am the boss.")

print_hello()  
# Recursion
def show(n):
    if(n==1):
        return
    print(n)
    show(n-1)  
show(10)    

def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(10))    
    
    