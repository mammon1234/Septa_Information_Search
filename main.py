#! /usr/bin/env python
#! encoding:utf-8
from Tkinter import *
import tkMessageBox
import ttk
from time import sleep
from selenium import webdriver
import clienttry

root=Tk()
root.title("SEPTA")
def callback():   
    d1=v1.get()
    d2=v2.get()
    d3=v3.get()
    d4=dora.box_value.get()
    if d4=='Depart':
        d4='D'
    else:
        d4='A'
    d6=v6.get()
    pstring=d1+','+d2+','+d3+','+d4+','+d6
    print pstring
    sget=clienttry.client(d1+','+d2+','+d3+','+d4+','+d6)
    print sget
    tkMessageBox.showinfo("Python command",sget)
class DorA:
    def __init__(self, parent):
        self.parent = parent
        self.combo()
    def combo(self):
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.parent, textvariable=self.box_value, state='readonly')
        self.box['values'] = ('Depart', 'Arrive')
        self.box.current(0)
        self.box.grid(row=1,column=2)
        
v1=StringVar()
v2=StringVar()
v3=StringVar()
v6=StringVar()
Label(root, text="Starting Station",
        bg="red",width=30,height=2,
        wraplength=80,justify="left").grid(row=0,column=0)
Entry(root, width=30,textvariable=v1).grid(row=0,column=1)
v1.set("Claymont")
Label(root, text="Destination Station",
        bg="red",width=30,height=2,
        wraplength=80,justify="left").grid(row=1,column=0)
Entry(root, width=30,textvariable=v2).grid(row=1,column=1)
v2.set("Trenton")
dora=DorA(root)
Label(root, text="Schedule Time",
        bg="red",width=30,height=2,
        wraplength=80,justify="left").grid(row=2,column=0)
Entry(root, width=30,textvariable=v3).grid(row=2,column=1)
v3.set("11:59PM")
Label(root, text="Schedule Data",
        bg="red",width=30,height=2,
        wraplength=80,justify="left").grid(row=3,column=0)
Entry(root, width=30,textvariable=v6).grid(row=3,column=1)
v6.set("04/30/2015")
Button(root, text="Run", fg="blue",bd=2,width=28,command=callback).grid(row=4)
root.mainloop()

