'''
Program to define a function to generate a Fibonacci series of the user input length.
'''

def fib():
    x=0
    y=1
    a=int(input("Enter the length of the series: "))
    print(x)
    print(y)
    for n in range(3,a+1):
        z=x+y
        print(z)
        x=y
        y=z
fib()