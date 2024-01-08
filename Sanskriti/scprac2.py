'''
Program defining functions for addition, subtraction and verifying whether the user input is odd or even with parameters (and arguments).
'''

def add(x:int,y:int):
    z=x+y
    print(x,"+",y,"=",z)

def sub(x:int,y:int):
    z=x-y
    print(x,"-",y,"=",z)
    
def evenodd(x:int):
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
    n1=int(input("Enter n1:"))
    n2=int(input("Enter n2:"))
    if f==1:
        add(n1,n2)
    elif f==2:
        sub(n1,n2)
    elif f==3:
        evenodd(n1)
        evenodd(n2)
    else:
        print("invalid input")
    c=input("Would you like to continue? ")

