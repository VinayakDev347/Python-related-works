# #tkinter
# """
# from tkinter import *

# root = Tk()                                             

# screen = Label(root,text="Hello World",bg="red")
# screen.pack()
# Label(root,text="hellow vinayak").pack()

# root.mainloop()
# """
# from tkinter import *
# root = Tk()

# f = Frame(root)
# f.pack()
# def fun():
#     print("you have clicked here!!!")
# def cancel():
#     print("Its cancelled")

# Label(f,text="Are You There?",fg="blue").pack()
# Button(f,text="Im here!!!",bg="yellow",command=fun).pack()
# Button(f,text="Buzyy!!!",bg="red",command=cancel).pack()

# root.mainloop()
#----------------------------------

#input position with the help of grid method
"""from tkinter import *

root = Tk()

Label(root,text="Enter Your User name: ").grid(row=0,column=0)
Entry(root).grid(row=0,column=1)
Label(root,text="Enter Your Password: ").grid(row=1,column=0)
Entry(root).grid(row=1,column=1)

root.mainloop()"""

#Tkinter Self adjacent widget
"""from tkinter import*

root = Tk()

Label(root,text="x direction",bg="red").pack(side=LEFT,fill=X)
Label(root,text="y direction",bg="cyan").pack(side= LEFT,fill=Y)
root.mainloop()"""

#Tkinter Class
"""from tkinter import*

root = Tk()

class demo:
    def __init__(self,rootone):
        frame = Frame(rootone)
        frame.pack()
        self.p = Button(frame,text = "click here",command=self.print_msg)
        self.p.pack()
        Button(frame,text="exit",command=frame.quit).pack()

    def print_msg(self):
        print("Welcome..")

obj = demo(root)
root.mainloop()"""

#Tkinter Messagebox
"""from tkinter import*
import tkinter.messagebox 
root = Tk()

# tkinter.messagebox.showinfo("title","this is information")
# tkinter.messagebox.showwarning("title","this is Warning")
# tkinter.messagebox.showerror("title","this is Error")
# tkinter.messagebox.askquestion("title","this is Question")
# tkinter.messagebox.askokcancel("title","this is askokcancel")
# tkinter.messagebox.askretrycancel("title","this is askretrycancel")

root.mainloop()"""

#Tkinter dropdown
"""from tkinter import*

root = Tk()

def fun():
    print("Saved")

mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)
mymenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="save",command=fun)
submenu.add_separator()
submenu.add_command(label="exit",command=root.quit)

newmenu = Menu(mymenu)
mymenu.add_cascade(label="edit",menu=newmenu)
newmenu.add_command(label="undo",command=fun)
newmenu.add_separator()
newmenu.add_command(label="undo")
newmenu.add_separator()

root.mainloop()
#
"""


import  tkinter as tk

def click(event):
    current = display.get()
    text = event.widget.cget('text')

    if text == '=':
        result = eval(current)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    elif text == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, text)

window = tk.Tk()
window.title("MY Calculator")

display = tk.Entry(window,font=("Arial",25))
display.pack(fill=tk.X,padx=10,pady=10,ipady=10)


btn_frame = tk.Frame(window)
btn_frame.pack()


button_labels = [
    "7" , "8" , "9" , "+" ,
    "4" , "5" , "6" , "-" ,
    "1" , "2" , "3" , "*" ,
    "C" , "0" , "=" , "/" , 

]
 
i = 0
for label in button_labels:
    button = tk.Button(btn_frame, text=label, font=("Arial",18), padx=20, pady=20)
    button.grid(row=i//4, column=i%4, padx=10, pady=10 )
    button.bind("<Button-1>", click)
    i += 1
# button7 = tk.Button(btn_frame,text="7",font=("Arial",20))
# button7.grid(row=0,column=0)

# button7 = tk.Button(btn_frame,text="8",font=("Arial",20))
# button7.grid(row=0,column=1)

# button7 = tk.Button(btn_frame,text="9",font=("Arial",20))
# button7.grid(row=0,column=2)

# button7 = tk.Button(btn_frame,text="+",font=("Arial",20))
# button7.grid(row=0,column=3)
window.mainloop()



