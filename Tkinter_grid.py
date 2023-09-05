from tkinter import *
root = Tk()
root.geometry('250x250')
username = Label(root,text="Username").grid(rows=1,column=1)
t1=Entry(root).grid(rows=1,column=3)
password = Label(root,text="Password").grid(rows=1,column=1)
t2=Entry(root).grid(rows=2,column=3)
b1=Button(root,text="Login").grid(rows=3,column=3)

root.mainloop()
