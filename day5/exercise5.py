print(".......exercise 1.......")
class Employee:
    def __init__(self,Employeenumber,name,address,salary,jobTitle):
        self.Employeenumber = Employeenumber
        self.__name = name
        self.__address = address
        self.__salary = salary
        self.__jobTitle = jobTitle
        
    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
    
    def setAddress(self,n):
        self.__address = n
        
    def getSalary(self):
        return self.__salary
    
    def getJobTitle(self):
        return self.__jobTitle
    
    def print1(self):
        print(". Employee1 information: ")
        print(". Employee_Number: ", self.Employeenumber)
        print(".Name: ",self.__name )
        print(".Addres: ",self.__address )
        print(".Salary: ", self.__salary)
        print(".Job_title: ", self.__jobTitle)
        
    def print2(self):
         print(". Employee2 information: ",". Employee_Number: ", self.Employeenumber, ".Name: ",self.__name,".Addres: ",self.__address, ".Salary: ", self.__salary, ".Job_title: ", self.__jobTitle)
    
    def __del__( self ):
        print ( self.__name,"has been deleted")
        
"""        
noor=Employee(1,"Noor",'gggg',150,'kkkk')
print(noor.getAddress())
del noor
"""

print(".......exercise 2.......")
Employee1=Employee(1,'Mohammad Khalid','Amman,Jordan',500,'Consultant')
Employee2=Employee(2,'Hala Rana','Aqaba,Jordan',750,'Manager')


print(".......exercise 3.......")
Employee1.setAddress("USA")
print("Employee1 New Address : ",Employee1.getAddress())


print(".......exercise 4.......")
del Employee1
del Employee2



  
        
    