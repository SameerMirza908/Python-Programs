from tkinter import *
from PIL import ImageTk,Image
root = Tk()


root.iconbitmap('C:/Users/de/.spyder-py3/cheff1.png')
e = Entry(root , width=30,  borderwidth=6)
e.pack()

r = StringVar()
r.set("Male")
def myclick():
    mylabel3 = Label(root,text="Hello sir "+e.get())
    mylabel3.pack()

def mygender(value):
    mylabel4 = Label(root,text="Gender "+value)
    mylabel4.pack()
    

mylabel = Label(root,text="Hello world!!!")
mylabe2 = Label(root,text="My name is sameer")

mybutton = Button(root,text="Enter your name", command=myclick)

mybutton1 = Button(root, text="Exit", command=root.quit)

mybutton2 = Button(root, text="OK", command=lambda : mygender(r.get()))

mylabel4 = Label(root,text=r.get())
mylabel4.pack()

Radiobutton(root , text="Male",variable=r, value="Male", command=lambda : mygender(r.get())).pack()
Radiobutton(root , text="Female",variable=r, value="Female", command=lambda : mygender(r.get())).pack()

mybutton2.pack()
mybutton.pack()
mylabel.pack()
mylabe2.pack()
mybutton1.pack()
mylabel3.pack()

root.mainloop()







