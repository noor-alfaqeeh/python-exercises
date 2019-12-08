from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkinter import messagebox, scrolledtext


window = Tk()
window.title("Employee Application")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width = 900
height = 500

#<<<<<<<<<<<<<<< VARIABLES>>>>>>>>>>>>>>>>>>>>>>


#<<<<<<<<<<<<<<< METHODS >>>>>>>>>>>>>>>>>>>>>>>
def Database():
    global conn, c
    conn = sqlite3.connect('OrgDB.db')
    c = conn.cursor()
    """
    c.execute('''CREATE TABLE  EmployeesTable 
                 (EmployeeNumber INT, EmployeeName TEXT, EmployeeGender TEXT, EmployeeNationality TEXT, EmployeeDateofBirth TEXT, EmployeeAddress TEXT, EmployeeDepartment TEXT, EmployeeSalary REAL)''')
    print ('Data base created')
    """
    
    
    
#<<<<<<<<<<<< Add Employee >>>>>>>>>>>>
        
def AddEmp():
    addEmp = Toplevel(window)
    
    EmployeeNumber = IntVar()
    EmployeeName = StringVar()
    EmployeeGender  = StringVar()
    EmployeeNationality = StringVar()
    EmployeeDateofBirth = StringVar()
    EmployeeAddress = StringVar()
    EmployeeDepartment = StringVar()
    EmployeeSalary = IntVar()
    
    
    number = Label(window, text = "Employee Number").grid(row=0, column = 0)
    e1 = Entry(window, textvariable= EmployeeNumber).grid(row = 0, column =1)
    
    name = Label(window, text = "Name").grid(row=1, column = 0)
    e2 = Entry(window, textvariable= EmployeeName).grid(row = 1, column =1)
    
    gender = Label(window, text = "Gender").grid(row=2, column = 0)
    e3 = Entry(window, textvariable= EmployeeGender).grid(row = 2, column =1)
    
    nationality = Label(window, text = "Nationality").grid(row=3, column = 0)
    e4 = Entry(window, textvariable= EmployeeNationality).grid(row = 3, column =1)
    
    dateofBirth = Label(window, text = "Date of Birth").grid(row=4, column = 0)
    e4 = Entry(window, textvariable= EmployeeDateofBirth).grid(row = 4, column =1)
    
    address = Label(window, text = "Address").grid(row=5, column = 0)
    e5 = Entry(window, textvariable= EmployeeAddress).grid(row = 5, column =1)
    
    Department = Label(window, text = "Department").grid(row=6, column = 0)
    e5 = Entry(window, textvariable= EmployeeDepartment).grid(row = 6, column =1)
    
    Salary = Label(window, text = "Salary").grid(row=7, column = 0)
    e5 = Entry(window, textvariable= EmployeeSalary).grid(row = 7, column =1)
    
    def Add():
        if EmployeeNumber.get()=="" or EmployeeName.get() == "":
            print("Please enter the Employee number and name feilds")
            
        else:
            Database()
            c.execute("INSERT INTO EmployeesTable (EmployeeNumber, EmployeeName, EmployeeGender, EmployeeNationality, EmployeeDateofBirth, EmployeeAddress, EmployeeDepartment, EmployeeSalary) VALUES(?, ?, ?, ?, ?, ?,?,?)", (str(EmployeeNumber.get()), str(EmployeeName.get()),str(EmployeeGender.get()) ,str(EmployeeNationality.get()), str(EmployeeDateofBirth.get()), str(EmployeeAddress.get()), str(EmployeeDepartment.get()),str(EmployeeSalary.get())))
            conn.commit()
            c.execute("SELECT * FROM EmployeesTable")
            for row in c:
                print (row)
                
            #conn.close()
            
            EmployeeNumber.set("")
            EmployeeName.set("")
            EmployeeGender.set("")
            EmployeeNationality.set("")
            EmployeeDateofBirth.set("")
            EmployeeAddress.set("")
            EmployeeDepartment.set("")
            EmployeeSalary.set("")
            #conn.close()
            print("Created a data!")
        
    save = Button(window, text="Add", command= Add).grid(row =9, column = 0)
    end = Button(window, text="Exit", command= window.destroy).grid(row =9, column = 1)
    
    
    
def view():
    Database()
    #c = conn.cursor()
    c.execute("SELECT * FROM EmployeesTable")
    
    addwin=Toplevel(window)
    addwin.title('view')
    txt = scrolledtext.ScrolledText(addwin, width=100, height=100)
    
    for row in c:
        txt.insert(END,row)
        txt.insert(END,"\n")
    
    txt.yview(END)
    txt.pack()
    conn.commit() 
    
    
        
        
def notdone():
    messagebox.showinfo('Not implemented', 'Not yet available')
    
    
    
    
    
    
    
    
    
    
    
top = Menu(window)
window.config(menu=top)


file = Menu(top,tearoff=0)
file.add_command(label='Quit', command=window.destroy)
top.add_cascade(label='File', menu=file)


Employee = Menu(top,tearoff= 0)
Employee.add_command(label='Add', command=AddEmp)
Employee.add_command(label='View' ,command=view)
top.add_cascade(label='Employee', menu=Employee)



window.mainloop()