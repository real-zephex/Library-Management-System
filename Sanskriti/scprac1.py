'''
Program defining functions for addition, subtraction and verifying whether the user input is odd or even with no parameters.
'''

def add():
    x=int(input("Enter x:"))
    y=int(input("Enter y:"))
    z=x+y
    print(x,"+",y,"=",z)

def sub():
    x=int(input("Enter x:"))
    y=int(input("Enter y:"))
    z=x-y
    print(x,"-",y,"=",z)
    
def evenodd():
    x=int(input("Enter x:"))
    if x%2==0:
        print(x,"is an even number.")
    else:
        print(x,"is an odd number.")
 
c="y"       
while c=="y" or c=="yes" :
    print("enter 1 for addition")
    print("enter 2 for subtraction") 
    print("enter 3 for evenodd")
    f=int(input("Enter your function choice: "))
    print ("Your choice is: ",f)
    if f==1:
        add()
    elif f==2:
        sub()
    elif f==3:
        evenodd()
    else:
        print("invalid input")
    c=input("Would you like to continue? ")

