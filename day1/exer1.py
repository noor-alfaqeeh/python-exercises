#ex1:
print('Hello','\t Hello','\t\t Hello', sep='\n')

#ex2:
print('Orange Academy \n'*20)

#ex3:
x=float(1)
y=float(2.8)
z=float("3")
w=float("4.2")
print(x,y,z,w,sep='10')
#1.0102.8103.0104.2

#ex4:
val1=int(input("Enter first value? "))
val2=int(input("Enter second value? "))
print(val1*val2)

#ex5:
value1=int(input("Enter value? "))
value2=int(input("Enter  value? "))
value3=int(input("Enter  value? "))
value4=int(input("Enter value? "))
value5=int(input("Enter value? "))

print((value1+value2+value3+value4+value5)/5)


#ex6:
x=1
y=2.8
z=1j
o="Orange"
A=True
print(type(x)) #<class 'int'>
print(type(y)) #<class 'float'>
print(type(z)) #<class 'complex'>
print(type(o)) #<class 'str'>
print(type(A)) #<class 'bool'>

#ex7:
x,y="Orange",1
X1,y1=100,-10
print(x) #Orange
print(y) #1
print(x1)
print(y1) # #NameError: name 'x1' is not defined

#ex8:
x=10
print(x)
X_q="Orange"
print(X_q)
AB=14
print(AB)
print("10"*10)

#ex9,10:
#repeated

#ex11:
#print("Hello World!")
print("Cheers, Mate!") #This is the program
"""Testing
The Code
"""
#Cheers, Mate!

#ex12:

name=input("Enter Your name? ")
age=int(input("Enter you age? "))
print((100-age)+2019)

#ex13:

base=int(input("Enter triangle base? "))
height=int(input("Enter triangle height? "))
print( 0.5*base*height)

#ex13:
x=11
y=3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(abs(x*-1))
print(int(x))
print(float(x))
print(divmod(x,y))
print(pow(x,y))
print(x**y)
print(x>y)
print(x==y)
print(x!=y)
"""
14
8
33
3.6666666666666665
3
2
11
11
11.0
(3, 2)
1331
1331
True
False
True
"""