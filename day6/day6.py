from functools import reduce

class Person:
    def __init__(self,name,address):
        self._name=name
        self._address=address
        
    def getName(self):
        return self._name
    
    def setName(self,newName):
        self._name=newName
        
    def getAddress(self):
        return self._address
    
    def setAddress(self,newAddress):
        self._address=newAddress
        
    def __del__(self):
        print('I have been deleted !')
        
        
class Employee(Person):
    def __init__(self,employeeNumber,name,address,salary,jobTitle,loans):
        self.employeeNumber=employeeNumber
        self.setName(name)
        self.setAddress(address)
        self.__salary=salary
        self.__jobTitle=jobTitle
        self.__loans=loans
        
    def getSalary(self):
        return self.__salary
    
    def setSalary(self,newSalary):
        self.__salary=newSalary
        
    def getJobTitle(self):
        return self.__jobTitle
    
    def setJobTitle(self,newTitle):
        self.__jobTitle=newTitle
        
    def getLoan(self):
        return self.__loans
        
    def getTotalLoans(self):
        totalLoans=reduce(lambda x,y: x+y,self.__loans)
        return totalLoans
    
    def setLoans(self,newLoans):
        self.__loans=newLoans
        
    def getMaxLon(self):
        maxLon=reduce(lambda x,y: x if x>y else y, self.__loans)
        return maxLon
    
    def getMinLon(self):
        minLon=int(reduce(lambda x,y: x if x<y else y, self.__loans))
        return minLon
    
    def getLoans(self):
        return self.__loans
    
    def printInfo(self):
        print('Employee Informations: \n','Employee Number:',self.employeeNumber,',Salary:',self.getSalary(),',Job Title:',self.getJobTitle(),',Loans:',self.getLoan(),',Total Loans:',self.getTotalLoans())
        
    def __del__(self):
        print('I have been deleted !')
        


  
class Student(Person):
    def __init__(self, Student_Number,name,address, Subject, Marks):
        self.Student_Number = Student_Number
        self.__Subject = Subject
        self.__Marks = Marks
        self.setName(name)
        self.setAddress(address)   
        
    def getSubject(self):
        return self.__Subject
    def setSubject(self, Subject):
        self.__Subject =  Subject
    def getMarks(self):
        return self.__Marks
    def setMarks(self, Marks):
        self.__Marks =  Marks
    def getAverage(self):
        sum=0
        n=0
        for key in self.__Marks:
            sum += self.__Marks[key]
            n+=1
        return  sum/n
    
   
    
    def getAMarks(self):
        return list(filter(lambda x: (x>=90),(self.__Marks).values()))
    
    def printinfo(self):
        print('Student Informations: \n','Student Number:',self.Student_Number,',Student Name:',self.getName(),',Student Address:',self.getAddress(),',Student Subject:',self.getSubject(),',Student Marks:',self.getMarks(),',Student Average:',self.getAverage())
        
    def __del__(self):
        print(" I have deleted ")
        
        

        
        
Employee1=Employee(1000,'Ahmad Yazen','Amman, Jordan',500,'HR Consultant',[434,200,1020])
Employee2=Employee(2000,'Hala Rana','Aqaba, Jordan',750,'Department Manager',[150,3000,250])
Employee3=Employee(3000,'Mariam Ali','Mafraq, Jordan',600,'HR S Consultant',[304,1000,250,300,500,235])
#Employee4=Employee(4000,'Yasmeen Mohammad','Karak, Jordan',865,'Diroctor')



Student1=Student(20191000,'Khalid Ali','Irbid,Jordan','History',{'English=':80,'Arabic=':90,'Art=':95,'Management=':75})
Student2=Student(20182000,'Reem Hani','Zarqa,Jordan','Software Eng',{'English=':80,'Arabic=':90,'Management=':75,'Calculus=':85,'OS=':73,'Programming=':90})
Student3=Student(20161001,'Nawras Abdullah','Amman,Jordan','Arts',{'English=':83,'Arabic=':92,'Art=':90,'Management=':70})
Student4=Student(20172030,'Amal Raed','Tafelah,Jordan','Computer Eng',{'English=':83,'Arabic=':92,'Management=':70,'Calculus=':80,'OS=':79,'Programming=':91})


#1   
EmployeeList=[Employee1,Employee2,Employee3]
#2
StudentsList=[Student1,Student2,Student3,Student4]


#3
def numEmployees(self):
    print('Total Number of Employees: ',len(EmployeeList))
    
#4    
def numStudents(self):
    print('Total Number of Students: ',len(StudentsList))
    
#5    
def employeeInfo(list):
    for x in list:
        print(x.printInfo())
        
#6        
def studentInfo(list):
    for y in list :
        print(y.printinfo())
#7
allAvg=[]
for student in StudentsList:
    allAvg.append(student.getAverage())
highestAvg=reduce(lambda x,y: x if x>y else y,allAvg)
print(highestAvg)


#8
        
def minLoan(list):
    loans=[]
    for i in list:
        loans.append(i.getMinLon())
    print(min(loans))
    
    
    
#9
def maxLoan(list):
    loans=[]
    for i in list:
        loans.append(i.getMaxLon())
    print(max(loans))
    
    
    
#10
allLoans=[]
avgLoans=[]
for employee in EmployeeList:
    allLoans.append(employee.getLoans())
    avgLoans.append(employee.getTotalLoans())
    totalLoans=reduce(lambda x,y: x+y,avgLoans)
print('\nList of employee loans:',allLoans,'Total for each employee:',avgLoans,'Grand total loans across all employees:',totalLoans,sep='\n')


    
#11
LoanDictionary = {}
for q in EmployeeList:
    LoanDictionary[q.employeeNumber]= q.getLoan()
#print(LoanDictionary)


#12
def readLoans(dictionary):
    
    for x in dictionary.values():
        print('Lowest Loan: ',reduce(lambda a,b : a if a < b else b,x))
        print('Highest Loan: ',reduce(lambda a,b : a if a > b else b,x))
        
        
#13:
def AScore(list):
    for x in list:               
        print('Name is ',x.getName(),',Subject is ', x.getSubject(), ', Marks are: ', x.getAMarks())    


#14
def maxSalary(list):
    salary=[]
    for i in list:
        salary.append(i.getSalary())
    print(max(salary))
        
#15:
def minSalary(list):
    salary=[]
    for i in list:
        salary.append(i.getSalary())
    print(min(salary))
    
#16:
def sumSalary(list):
    salary=[]
    for i in list:
        salary.append(i.getSalary())
    print(sum(salary))
    
    
#17:
for x in StudentsList:
    x.__del__()
for y in EmployeeList:
    y.__del__()

    
       
       

numEmployees(EmployeeList)
numStudents(StudentsList)
print(EmployeeList)
print(Student1.printinfo())
print(StudentsList)
employeeInfo(EmployeeList)
studentInfo(StudentsList)
minLoan(EmployeeList)
print(Employee1.getMinLon())
maxLoan(EmployeeList)
readLoans(LoanDictionary)
AScore(StudentsList)
print(Student1.getMarks())
maxSalary(EmployeeList)
minSalary(EmployeeList)
sumSalary(EmployeeList)
        
