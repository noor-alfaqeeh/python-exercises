print("<<<<<<<<<<<<<< exercise1 >>>>>>>>>>>>>>>>")

num1=int(input("enter first number "))
num2=int(input("enter second number "))
if num1>num2:
    print(num1)
else:
    print(num2)


print("<<<<<<<<<<<<<< exercise2 >>>>>>>>>>>>>>>>")
num=int(input("Input a number: "))
for a in range(1,11):
    print(num,'*',a,'=',num*a)
    
    

print("<<<<<<<<<<<<<< exercise3 >>>>>>>>>>>>>>>>")
for a in range(6):
    for b in range(a):
        print("*",end="")
    print("")
for c in range(4,0,-1):
    for d in range(c):
        print("*",end="")
    print("")
    

print("<<<<<<<<<<<<<< exercise4 >>>>>>>>>>>>>>>>")
letters=["x","y","z","a","b","c"]
for i in letters:
    if i == "a":
        continue
    elif i=="c":
        break
    print(i)
    
"""
The Output:
x
y
z
b
"""

print("<<<<<<<<<<<<<< exercise5 >>>>>>>>>>>>>>>>")
for x in range(12,25,3):
    print(x)
    
"""
The Output:
12
15
18
21
24
"""
    
    
print("<<<<<<<<<<<<<< exercise6 >>>>>>>>>>>>>>>>")
i=1
while i<6:
    print(i)
    if i == 3:
        break
    i+=1

"""
The Output:
1
2
3
"""

print("<<<<<<<<<<<<<< exercise7 >>>>>>>>>>>>>>>>")
num=int(input("Input a number: "))
x=0
for n in range(0,num):
    x+=n
print(x)


print("<<<<<<<<<<<<<< exercise8 >>>>>>>>>>>>>>>>")
number=int(input("Input a number: "))
if number%2 == 0:
    print("It's an even number")
else:
    print("It's an odd number")

print("<<<<<<<<<<<<<< exercise9 >>>>>>>>>>>>>>>>")
for x in range(10):
     for y in range(9-x):
         print (' ',end='')  
     for z in range(0,x,1):
         print (z+1,end='')
     for w in range(x-1,0,-1):
         print (w,end='')
     print()
for a in range(9,0,-1):
     for b in range(10-a):
         print (' ',end='')    
     for c in range(1,a,1):
         print (c,end='')
     for d in range(a-1,1,-1):
         print (d-1,end='')
     print()

  
print("<<<<<<<<<<<<<< exercise10 >>>>>>>>>>>>>>>>")
while True:
     try:
        num = input("Please enter an integer number : ")
        num = int(num)
        break
     except ValueError:
         print("No valid integer! Please try again ...")
print("you entered an integer number: ",num)

 
print("<<<<<<<<<<<<<< exercise11 >>>>>>>>>>>>>>>>") 
try:
    a=3
    if a<4:
        b=a/(a-3)
    print("Value of b =",b)
except(ZeroDivisionError, NameError):
    print("\nError Occurred and Handled")
#Error Occurred and Handled