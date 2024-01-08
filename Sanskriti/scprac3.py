'''
Program defining functions for addition, subtraction and verifying whether the user input is odd or even with parameters (and arguments) and return.
'''

def add(x:int,y:int):
    z=x+y
    return z

def sub(x:int,y:int):
    z=x-y
    return z
    
def evenodd(x:int):
    if x%2==0:
        return 1
    else:
        return 3

c="y"       
while c=="y" or c=="yes" :
    print("enter 1 for addition")
    print("enter 2 for subtraction") 
    print("enter 3 for evenodd")
    f=int(input("Enter your function choice: "))
    print ("Your choice is: ",f)
    n1=int(input("Enter n1:"))
    n2=int(input("Enter n2:"))
    if f==1:
        a=add(n1,n2)
        print(n1,"+",n2,"=",a)
    elif f==2:
        a=sub(n1,n2)
        print(n1,"-",n2,"=",a)
    elif f==3:
        a=evenodd(n1)
        b=evenodd(n2) 
        if a==1:
            print(n1,"is an even number.")
        else:
            print(n1,"is an odd number.")
        if b==1:
            print(n2,"is an even number.")
        else:
            print(n2,"is an odd number.")
    else:
        print("invalid input")
    c=input("Would you like to continue? ")

