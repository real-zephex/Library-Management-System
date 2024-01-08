'''
Program to count the no. of "Me" or "My" words preset in a file story.txt. If the story.txt contents are as follows:
My first book 
was Me and
My Family. It
gave Me
a chance to be
Known to the 
world.
--------------
The output should read :
Total no. of Me and My=  4
'''

def countMeMy():
    num=0
    f=open("story.txt","r")
    n=f.read()
    m=n.split()
    for x in m:
        if x == "Me" or x == "My" :
            num=num+1
    f.close()
    print("Total no. of Me and My= ", num)

countMeMy()