#
from tkinter import *
root = Tk()
root.geometry("500x400")

def getvls():
    print("it works")
    print("submit the form")
    print(f"{avalue.get(),bvalue.get(),cvalue.get(),dvalue.get(),evalue.get(),fvalue.get(),gvalue.get()}")
    
    
    
    with open("records11.txt","a") as f:
        f.write(f"{avalue.get(),bvalue.get(),cvalue.get(),dvalue.get(),evalue.get(),fvalue.get(),gvalue.get()}\n")
Label(root , text="PLEASE FILL THE FORM",font="comicsansns 10 bold").grid(row=0,column=3)

a=Label(text="fname:-",font = "comicsansns 10 bold",fg="black")
b=Label(text="lname:-",font = "comicsansns 10 bold",fg="blue")
c=Label(text="age:-",font = "comicsansns 10 bold",fg="green")
d=Label(text="exp:-",font = "comicsansns 10 bold",fg="pink")
e=Label(text="K.D:-",font = "comicsansns 10 bold",fg="brown")
f=Label(text="tier:-",font = "comicsansns 10 bold",fg="red")
a.grid(row = 1 , column = 2)
b.grid(row = 2 , column = 2)
c.grid(row = 3 , column = 2)
d.grid(row = 4 , column = 2)
e.grid(row = 5 , column = 2)
f.grid(row = 6 , column = 2)

avalue= StringVar()
bvalue= StringVar()
cvalue= StringVar()
dvalue= StringVar()
evalue= IntVar()
fvalue= StringVar()
gvalue= IntVar()  #checkbox ki vlue ya to 0 hogi ya to 1 hogi...
aentry= Entry(root,textvariable=avalue)
bentry= Entry(root,textvariable=bvalue)
centry= Entry(root,textvariable=cvalue)
dentry= Entry(root,textvariable=dvalue)
eentry= Entry(root,textvariable=evalue)
fentry= Entry(root,textvariable=fvalue)
aentry.grid(row=1,column=3)
bentry.grid(row=2,column=3)
centry.grid(row=3,column=3)
dentry.grid(row=4,column=3)
eentry.grid(row=5,column=3)
fentry.grid(row=6,column=3)
#check buttons:-
g=Checkbutton(text="DO YOU USE IPHONE 12 ",variable=gvalue)
g.grid(row=7,column=3)
Button(text="submit",command=getvls).grid(row=8,column=3)
root.mainloop()