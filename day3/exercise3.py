print('>>>>>>>>>>>>>> Exercise 1 >>>>>>>>')
nList=[1,5,20,8,10,-1]
for x in nList:
    print(x)
    
    
    
print('>>>>>>>>>>>>>> Exercise 2 >>>>>>>>')
print(sum(nList))



print('>>>>>>>>>>>>>> Exercise 3 >>>>>>>>>')
print(max(nList))



print('>>>>>>>>>>>>>>> Exercise 4 >>>>>>>')
a = [10,20,30,20,10,50,60,40,80,50,40]
print(list(set(a)))



print('>>>>>>>>>>>>>> Exercise 5 >>>>>>>>>>')
a = [10,20,30,20,10,50,60,40,80,50,40]
if len(a) >0:
    print("It is not empty")
else:
    print("It is Empty")
    
    
    
print('>>>>>>>>>>>>>> Exercise 6 >>>>>>>>>>')
t=('Noor','m','t',1,8,45)
for x in t:
    print(x)
    
    
    
print('>>>>>>>>>>>>> Exercise 7 >>>>>>>>>>')
num_set = set([0, 1, 2, 3, 4, 5])
for x in num_set:
    print(x)
    
    
    
print('>>>>>>>>>>>>> Exercise 8 >>>>>>>>>>')
s1={1,4,9,10}
s2={1,3,8,4}
print ( s1 & s2 )



print('>>>>>>>>>>>>> Exercise 9 >>>>>>>>>>')
setx= set(["green","blue"])
sety= set(["blue","yellow"])
seta= setx | sety
print(seta)
#{'green', 'yellow', 'blue'}



print('>>>>>>>>>>>>> Exercise 10 >>>>>>>>>>')
seta=set([5,10,3,15,2,20])
print(len(seta))
#6



print('>>>>>>>>>>>>> Exercise 11 >>>>>>>>>>')
dic={1:10,2:20}
dic1={3:30,4:40}
dic2={5:50,6:60}
dic4={}
for d in (dic,dic1,dic2):
    dic4.update(d)
print(dic4)
#{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}



print('>>>>>>>>>>>>> Exercise 12 >>>>>>>>>>')
a="Hello,World!"
print(a[1])
print(a[2:5])
print(a[-5:-2])
print(len(a))
print(a.lower())
print(a.replace("H","j"))
"""
e
llo
orl
12
hello,world!
jello,World!
"""






