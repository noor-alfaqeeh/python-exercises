print(".......exercise 1.......")
o=lambda x=1,y=2,z=3:x+y+z
print(o())
print(o(10))
print(o(10,20))
"""
6
15
33
"""

print(".......exercise 2.......")
import functools
nums=[5,10,45,2]
def multiplier(*num):
    print(functools.reduce(lambda a,b : a*b ,nums))
    
multiplier(nums)


print(".......exercise 3.......")
mult = lambda a, b : a * b
print ( mult(6,7) )

print(".......exercise 4.......")
less_than_zero = list(filter(lambda x: x<0 , range(-5,5)))
print(less_than_zero)

print(".......exercise 5.......")
x=lambda a,b,c : a+b+c
print(x(5,6,2))
# 13

print(".......exercise 6.......")
x=('Joey','Monica','Ross')
y=('Chandler','Pheobe')
z=('David','Rachel','Courtney')
result=list(zip(x,y,z))
print(result)
#[('Joey', 'Chandler', 'David'), ('Monica', 'Pheobe', 'Rachel')]

print(".......exercise 7.......")
coin=('Bitcoin','Ether','Ripple','Litecoin')
code=('BTC','ETH','XRP','LTC')
d=dict(zip(coin,code))
print(d)
#{'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}

print(".......exercise 8.......")
#function that filter vowels
def fun(variable):
    letters = ['a','e','i','o','u']
    if (variable in letters):
        return True
    else:
        return False
    
sequence = ['g','j','e','j','k','o','p','r']
filtered = list(filter(fun,sequence))
print(filtered)
#['e', 'o']

print(".......exercise 9.......")
x=list(map(int,input("Enter a multiple value:").split()))
print("List of students: ",x)
#List of students:  [1, 20, 10]

print(".......exercise 10.......")
def newfunc(a):
    return a*a
x = list(map(newfunc,(1,2,3,4)))
print(x)
#[1, 4, 9, 16]

print(".......exercise 11.......")
def func(a,b):
    return a+b
a=list(map(func,[2,4,5],[1,2,3,2,4]))
print(a)
#[3, 6, 8]

print(".......exercise 12.......")
c=map(lambda x: x+x,filter(lambda x: (x>=3),(1,2,3,4)))
print(list(c))
#[6, 8]

print(".......exercise 13.......")
c= filter(lambda x: (x>=3),map(lambda x: x+x,(1,2,3,4)))
print(list(c))
#[4, 6, 8]

print(".......exercise 14.......")
lis = [ 1 , 3, 5, 6, 2,15 ]
print ("The minimum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a < b else b,lis))
#The minimum element of the list is : 1

print(".......exercise 15.......")
numbers=[1,2,3]
letters=['a','b','c']
results = list(zip(numbers,letters))
print(results)
#[(1, 'a'), (2, 'b'), (3, 'c')]

 