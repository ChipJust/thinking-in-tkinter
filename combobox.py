#!python3
r""" combobox.py

https://tkdocs.com/tutorial/widgets.html#combobox

"""
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Combobox")

s = StringVar(value="On")    # default value is ''
b = BooleanVar(value=True)   # default is False
i = IntVar(value=10)         # default is 0
d = DoubleVar(value=10.5)    # default is 0.0

def comboboxSelected(*args):
    print("comboboxSelected({})".format(args))
    print("  s = {}".format(s.get()))
    cs.selection_clear()
    print("  b = {}".format(b.get()))
    cb.selection_clear()
    print("  i = {}".format(i.get()))
    ci.selection_clear()
    print("  d = {}".format(d.get()))
    cd.selection_clear()

cs = ttk.Combobox(root, textvariable=s)
cs.bind('<<ComboboxSelected>>', comboboxSelected)
cs['values'] = ('On', 'Off')
cs.grid()

cb = ttk.Combobox(root, textvariable=b)
cb.bind('<<ComboboxSelected>>', comboboxSelected)
cb['values'] = (True, False)
cb.grid()

ci = ttk.Combobox(root, textvariable=i)
ci.bind('<<ComboboxSelected>>', comboboxSelected)
ci['values'] = (10, 1)
ci.grid()

cd = ttk.Combobox(root, textvariable=d)
cd.bind('<<ComboboxSelected>>', comboboxSelected)
cd['values'] = (10.5, 2.3)
cd.grid()

root.mainloop()
