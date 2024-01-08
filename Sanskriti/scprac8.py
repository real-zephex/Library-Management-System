'''
Program which reads each character in a text file story.txt and displays and counts the occurence of each A or a and M or m. If the story.txt contents are as follows:
My first book 
Was me and
My family. It
Gave Me 
A chance to be
Known to the 
World.
'''

def amcount():
    l=0
    m=0
    f=open("story.txt",'r')
    n=f.read()
    for x in n:
        if x=="a" or x=="A" :
            print(x)
            l = l+1
        elif x=="m" or x=="M" :
            print(x)
            m = m+1
    f.close()
    print("Total no. of a or A= ",l)
    print("Total no. of m or M= ",m)
    
amcount()