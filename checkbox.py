#!python3
r""" checkbox.py

https://tkdocs.com/tutorial/widgets.html#checkbutton

"""
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Checkboxes")

s = StringVar(value="on")   # default value is ''
b = BooleanVar(value=True)   # default is False
i = IntVar(value=10)         # default is 0
d = DoubleVar(value=10.5)    # default is 0.0

def checkboxChanged(*args):
    print("checkboxChanged({})".format(args))
    print("  s = {}".format(s.get()))
    print("  b = {}".format(b.get()))
    print("  i = {}".format(i.get()))
    print("  d = {}".format(d.get()))

ttk.Checkbutton(
    root,
    text='StringVar',
    command=checkboxChanged,
    variable=s,
    onvalue='on',
    offvalue='off',
    ).grid()

ttk.Checkbutton(
    root,
    text='BooleanVar',
    command=checkboxChanged,
    variable=b,
    onvalue=True,
    offvalue=False,
    ).grid()

ttk.Checkbutton(
    root,
    text='IntVar',
    command=checkboxChanged,
    variable=i,
    onvalue=10,
    offvalue=1,
    ).grid()

ttk.Checkbutton(
    root,
    text='DoubleVar',
    command=checkboxChanged,
    variable=d,
    onvalue=10.5,
    offvalue=0.5,
    ).grid()


root.mainloop()
