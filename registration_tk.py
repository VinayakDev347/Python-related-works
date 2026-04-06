from tkinter import *
import tkinter
import tkinter.messagebox

t = Tk()
t.title('Registration')
t.geometry('700x500')

a = tkinter.Label(text='Registration Form',bg='indigo',fg='white',font=('times new roman',35,'bold'))
a.place(x=150,y=0)

b = tkinter.Label(text='First Name:',bg='yellow',fg='red',font=('bradley hand itc',25,'bold'))
b.place(x=20,y=80)  
c=tkinter.Entry(width=35)
c.place(x=300,y=95)

d = tkinter.Label(text='Last Name:',bg='yellow',fg='red',font=('bradley hand itc',25,'bold'))
d.place(x=20,y=130) 
e = tkinter.Entry(width=35)
e.place(x=300,y=145)


f=tkinter.Label(text='Phone No:',bg='yellow',fg='red',font=('bradley hand itc',25,'bold'))
f.place(x=20,y=180)   
g = tkinter.Entry(width=35)
g.place(x=300,y=195)

def submitting():
    tkinter.messagebox.showinfo('submitting page','Successfully Submitted')
    t.distroy()

h = tkinter.Button(text='Submit',bg='yellow',fg='red',font=('bradley hand itc',25,'bold'),command=submitting)
h.place(x=220,y=280)   



t.mainloop()