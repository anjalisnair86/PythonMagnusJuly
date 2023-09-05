from tkinter import *
root = Tk()

root.geometry('250x250')
lb = Button(root,text = "left",height=5,width=10,fg="green")
lb.pack(side=LEFT)
rb = Button(root,text = "right",height=5,width=10,fg = "blue")
rb.pack(side=RIGHT)
tb = Button(root,text="up",height=5,width=10,fg="yellow")
tb.pack(side=TOP)
bb = Button(root,text="down",height=5,width=10,fg="orange")
bb.pack(side=BOTTOM)
root.mainloop()

