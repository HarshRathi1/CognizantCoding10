'''Institution is offering a variety of courses to students. Students have a facility to check whether a particular course is available in the institution. Write a program to help the institution accomplish this task. If the number is less than or equal to zero display “Invalid Range”.

Assume maximum number of courses is 20.'''
n=int(input("Enter no of course:"))
c=[]
if n<=0 or n>20:
    print("Invalid Range")
else:
    for i in range(n):
        a=input("Enter cours names:")
        c.append(a)
s=input("Enter the course to be searched")
if s in c:
    print(s,"course is available")
else:
    print(s,"course is not available")