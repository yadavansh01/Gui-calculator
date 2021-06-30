from tkinter import *
f=Tk()

v=StringVar()
a=StringVar()
b=StringVar()
c=StringVar()
opt=StringVar()
            
def b1():
    v.set(v.get()+"1")
def b2():
    v.set(v.get()+"2")
def b3():
    v.set(v.get()+"3")
def b4():
    v.set(v.get()+"4")
def b5():
    v.set(v.get()+"5")
def b6():
    v.set(v.get()+"6")
def b7():
    v.set(v.get()+"7")
def b8():
    v.set(v.get()+"8")
def b9():
    v.set(v.get()+"9")
def b0():
    v.set(v.get()+"0")


def bp():
    a.set(v.get())
    v.set("")
    opt.set("+")
def bm():
    a.set(v.get())
    v.set("")
    opt.set("*")
def bs():
    a.set(v.get())
    v.set("")
    opt.set("-")
def bd():
    a.set(v.get())
    v.set("")
    opt.set("/")

def be():
    b.set(v.get())
    if(opt.get()=="+"):
        c=int(a.get())+int(b.get())
    elif(opt.get()=="-"):
        c=int(a.get())-int(b.get())
    elif(opt.get()=="*"):
        c=int(a.get())*int(b.get())
    elif(opt.get()=="/"):
        c=int(a.get())/int(b.get())
    v.set(c)
f.geometry("200x250")
f.resizable(0,0)
t1=Entry(textvariable=v).place(x=30,y=10)
b1=Button(text="1",command=b1).place(x=20,y=40)
b2=Button(text="2",command=b2).place(x=60,y=40)
b3=Button(text="3",command=b3).place(x=100,y=40)
b4=Button(text="4",command=b4).place(x=140,y=40)
b5=Button(text="5",command=b5).place(x=20,y=80)
b6=Button(text="6",command=b6).place(x=60,y=80)
b7=Button(text="7",command=b7).place(x=100,y=80)
b8=Button(text="8",command=b8).place(x=140,y=80)
b9=Button(text="9",command=b9).place(x=20,y=120)
b0=Button(text="0",command=b0).place(x=60,y=120)
be=Button(text="=",command=be,width=5).place(x=100,y=120)
bp=Button(text="+",command=bp).place(x=20,y=160)
bm=Button(text="*",command=bm).place(x=60,y=160)
bs=Button(text="-",command=bs).place(x=100,y=160)
bd=Button(text="/",command=bd).place(x=140,y=160)

f.mainloop()
