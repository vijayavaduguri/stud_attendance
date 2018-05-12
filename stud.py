import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import sqlite3
root=Tk()
conn=sqlite3.connect("students")
cur=conn.cursor()

    

def addclass():
    fr2.pack_forget()
    fr3.pack_forget()
    fr1.pack()
    

    
def addstu():
    fr1.pack_forget()
    fr3.pack_forget()
    fr2.pack()
   
    
    
    
    
def view():
    fr2.pack_forget()
    fr1.pack_forget()
    fr3.pack()
   
def insert():
    addstu()
    addclass()
   
    student_Id=stuid_text.get()
    Name=name_text.get()
    class_name=box_value.get()
    Mobile_no=mobi_text.get()
    Address=addr_text.get()
    #cur.execute("create table studentdetails (student_Id varchar(50),Name varchar(50),class_name varchar(10),mobile_no int(50),Address varchar(200))" )
    cur.execute("insert into studentdetails values(?,?,?,?,?)",(student_Id,Name,class_name,Mobile_no,Address))
    conn.commit()
    cur.execute("select * from studentdetails")
    row=cur.fetchall()
    print(row)

def upload():
    root.filename =  filedialog.askopenfilename(initialdir = "c:/Images",title = "choose your file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    #list1.insert(root.filename)
    print (root.filename)
    img = Image.open(root.filename)
    img=img.resize((150,150),Image.ANTIALIAS)
    im=ImageTk.PhotoImage(img)
    panel =tkinter.Label(fr2, image = im)
    panel.image= im
    panel.grid(row = 5, column = 155)


menu=Menu(root)
root.config(menu=menu)
a1=menu.add_cascade(label="Add class",command=addclass)
b=menu.add_cascade(label="Add students",command=addstu)
c=menu.add_cascade(label="View attendence",command=view)
##frame 1 add class
fr1=Frame(root)
fr1.pack()
l2=Label(fr1,text='classname')
l2.grid(row=0,column=10)
classn_text=StringVar()
e1=Entry(fr1,textvariable=classn_text)
e1.grid(row=0,column=11)


l3=Label(fr1,text='classteacher')
l3.grid(row=1,column=10)
classt_text=StringVar()
e3=Entry(fr1,textvariable=classt_text)
e3.grid(row=1,column=11)

b1=Button(fr1,text="Submit",width=12,command=insert)
b1.grid(row=15,column=10,columnspan=5)
##frame 2 add student
fr2=Frame(root)

b1=Button(fr2,text="upload",width=12,command=upload)
b1.grid(row=5,column=170,columnspan=5)
##frame 2 add student


l4=Label(fr2,text='student_Id')
l4.grid(row=0,column=0)
stuid_text=StringVar()
e4=Entry(fr2,textvariable=stuid_text)
e4.grid(row=0,column=1)


l5=Label(fr2,text='Name')
l5.grid(row=5,column=0)
name_text=StringVar()
e5=Entry(fr2,textvariable=name_text)
e5.grid(row=5,column=1)

l8=Label(fr2,text='class')
l8.grid(row=10,column=0)
box_value=StringVar()
com=ttk.Combobox(fr2,textvariable=box_value)
com.grid(row=10,column=1)
com['values']=('ECE-A','ECE-B','ECE-C')
com.current(0)

l9=Label(fr2,text='Mobile_no')
l9.grid(row=15,column=0)
mobi_text=StringVar()
e9=Entry(fr2,textvariable=mobi_text)
e9.grid(row=15,column=1)

la=Label(fr2,text='Address')
la.grid(row=20,column=0)
addr_text=StringVar()
ea=Entry(fr2,textvariable=addr_text)
ea.grid(row=20,column=1)

pic1=Label(fr2,text=' Photo', bg = 'white',height = 10, width = 20)
pic1.grid(row=5,column=155)


list2=Listbox(fr2,height=6,width=20)
list2.grid(row=15,column=155,columnspan=5)
lc=Label(fr2,text='Finger print')
lc.grid(row=15,column=150)

b1=Button(fr2,text="Submit",width=12,command=insert)
b1.grid(row=50,column=75,rowspan=5)
##frame 3 view
fr3=Frame(root)
l6=Label(fr3,text='Roll number')
l6.grid(row=50,column=100)
rollno_text=StringVar()
e6=Entry(fr3,textvariable=rollno_text)
e6.grid(row=50,column=101)

l7=Label(fr3,text='jkhdvc')
l7.grid(row=55,column=100)
name_text=StringVar()
e7=Entry(fr3,textvariable=name_text)
e7.grid(row=55,column=101)
