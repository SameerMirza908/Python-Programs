from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()

#r = IntVar()
#r.set("2")
#pizza = StringVar()
#for text, mode in MODES:
    #Radiobutton(root, text=text, variable=pizza, value=mode).pack()


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="C:\\Users\\de\\Downloads", title = "Select a file")
    myfile = Label(root , text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_label = Label(image=my_image).pack()
    

my_btn = Button(root , text="Open File" , command=open).pack()

    
e1 = Entry(root , width=20,  borderwidth=6)
e1.pack() 
   
e2 = Entry(root , width=20,  borderwidth=6)
e2.pack()

a = e1.get()
b = e2.get()


def myclick():  
    if e1.get() == "Sameer" and e2.get() == "admin":
        
      top = Toplevel()
      mylab = Label(top, text="Welcome to Weather App")
      mylab.grid(row=0 , column=0)
      top.geometry("400x400")
        
    else:
       
      messagebox.showerror("Error", "Invalid Username or Password")
   
    
   
var = IntVar()

cbutton = Checkbutton(root , text="Click the check boxes to choose" , variable=var , onvalue="1" , offvalue="0")
cbutton.pack()

cbutton.deselect()

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked, "monday","teusday", "wednesday")
drop.pack()


mybutton = Button(root , text="Click me", command=myclick)
mybutton.pack()

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

def slide():
    mylab1 = Label(root, text=vertical.get())
    mylab1.pack()
    label = Label(root, text=var.get()).pack()
    menulabel = Label(root , text=clicked.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))
    
btn = Button(root, text="Click here" , command=slide)
btn.pack()

root.mainloop()


