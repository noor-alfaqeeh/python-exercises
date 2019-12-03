print('...............exercise1...............')

from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.colorchooser import *

def act ():
     if value1.get() == "Orange" and value2.get() == "CodingAcademy" :
          z = messagebox.showinfo("Login", "Successful login")
          if z == "ok":
              parent.destroy()
     else:
          messagebox.showinfo("Login", "Wrong User Name or Password")
parent = Tk()
value1 = StringVar()
value2 = StringVar()
name = Label(parent, text = "Name").grid(row=0, column = 0)
e1 = Entry(parent, textvariable= value1).grid(row = 0, column =1)
password = Label(parent, text ="Password").grid(row = 1, column = 0)
e2 = Entry(parent, textvariable= value2).grid(row = 1, column =1)
submit = Button(parent, text="Submit", command= act).grid(row = 4, column = 0)
parent.mainloop()


print('...............exercise2...............')

q2=Tk(className="Question 2")

def openmsg():
    messagebox.showinfo("Q2", "This is a message")
    
def child1():
    c1=Toplevel(q2)
    c1.title("Child 1")
    Label(c1,text="Emp Number").grid(row=0,sticky=E)
    Label(c1,text="Emp Name").grid(row=1,sticky=E)
    x=StringVar()
    xx=StringVar()
    Entry(c1,textvariable=x).grid(row=0,column=1)
    Entry(c1,textvariable=xx).grid(row=1,column=1)
    Button(c1,text="Exit",command=c1.destroy).grid(row=2)



def child2():
    c2=Toplevel(q2)
    c2.title("Child 2")
    text=scrolledtext.ScrolledText(c2,width=40,height=10)
    text.insert('insert'," The count is 1 \n The count is 2 \n The count is 3 \n The count is 4 \n The count is 5 \n The count is 6 \n The count is 7 \n The count is 8 \n The count is 9 \n The count is 10 \n The count is 11 \n ")
    text.grid()

Button(q2,text="Open Message",command=openmsg).grid(row=0)
Button(q2,text="Open Child window 1",command=child1).grid(row=1)
Button(q2,text="Open Child window 2",command=child2).grid(row=2)
q2.mainloop()


print('...............exercise3...............')
win=Tk()
def getColor():
    color=askcolor()
    print(color)
    win.configure(background=color[1])
foo=Button(text="select color", command=getColor)
foo.pack()
win.mainloop()
