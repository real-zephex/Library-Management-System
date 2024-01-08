'''
Program to verify whether a 3 digit number is an Armstrong number or not.
'''

def armno(x:int,y:int,z:int):
    x3=x**3
    y3=y**3
    z3=z**3
    s=x3+y3+z3
    if s==int(n) :
        print("Yes,",int(n),"is an Armstrong number.")
    else:
        print("No,",int(n),"is not an Armstrong number.")
        
n=str(input("Enter the 3 digit number to be verified: "))

a=int(n[0])
b=int(n[1])
c=int(n[2])

armno (a,b,c)

