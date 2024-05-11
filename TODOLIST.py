import tkinter
from tkinter import *
#1 part
a=Tk()
a.title("CODSOFT_ToDoList")
a.geometry("400x550+400+200")
#functions
def ent():
    t=e.get()
    l.insert(END,"•"+t)
    e.delete(0,"end")
def Del():
    l.delete(ANCHOR)
#background
a.config(bg="MediumPurple1")

#lsitbox
f=Frame(a)
f.pack(pady=10)
l=Listbox(f,width=40,height=13,font=('Helvetica',12,'bold'),bg="Powder Blue",highlightthickness=0,selectbackground='gray29')
l.pack(side=LEFT,fill=BOTH,pady=8,padx=8)

pre_list=["CodSoft","Coding","Project"]

for i in pre_list:
    l.insert(END,"•"+i)

#enter

e=Entry(a,font=('Helvetica',12,'italic'),bg="Powder Blue",width=40)
e.pack(pady=10)
    
#button
btn1=Frame(a)
btn1.pack(pady=5)


btn_add=Button(btn1,text="  Add  ",font=("Helvetica",15,"bold"),bg="Powder Blue",padx=20,pady=0,command=ent)
btn_add.pack(fill=BOTH,expand=True,side=LEFT,pady=4,padx=5)

btn2=Frame(a)
btn2.pack(pady=5)
btn_dlt=Button(btn2,text="Delete",font=("Helvetica",15,"bold"),bg='Powder Blue',padx=20,command=Del)

btn_dlt.pack(fill=BOTH,expand=True,side=RIGHT,pady=4,padx=4)



a.mainloop()
