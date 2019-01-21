from array import *

a= int(input("Enter the number to find factorial: "))
arr = array('i',[])
i=1
while i <= a:
    arr.append(i)
    i+=1
x=1
for j in arr:
   x=x*j

print("The factorial of "+str(a)+" is "+str(x))