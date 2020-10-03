import wmi

from Tkinter import *

root=Tk()

"""
format for gettign into the classname , then iterate with getattr function which the
attribute iterator
c=wmi.WMI().classname()[0]
"""

"""enter the class name for the wmi query"""


e=raw_input('Enter classname ')
options=eval('wmi.WMI().'+e+'()[0]')
optionchosen=StringVar()

""" create a list of options from the wmi class that user entered"""
optionchosen.set(list(options.properties)[0])


""" here is your pop up menu"""
popupmenu=OptionMenu(root,optionchosen,*list(options.properties))
popupmenu.pack()



def print_class():
    
    classchosen=str(optionchosen.get())
    print getattr(options,classchosen,'') 

def myexit():
    root.destroy()
    exit()
b=Button(root,text="select class",command=print_class)

eb=Button(root,text='quit program',command=myexit)
b.pack()
eb.pack()

mainloop()













 
