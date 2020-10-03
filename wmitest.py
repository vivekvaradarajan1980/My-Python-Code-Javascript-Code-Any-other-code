import wmi

from Tkinter import *

root=Tk()

"""
format for gettign into the classname , then iterate with getattr function which the
attribute iterator
c=wmi.WMI().classname()[0]
"""

e=raw_input('Enter classname ')
options=eval('wmi.WMI().'+e+'()[0]')
optionchosen=StringVar()
optionchosen.set(list(options.properties)[0])
popupmenu=OptionMenu(root,optionchosen,*list(options.properties))
popupmenu.pack()



def print_class():
    
    classchosen=str(optionchosen.get())
    print getattr(options,classchosen,'') 

b=Button(root,text="select class",command=print_class)
eb=Button(root,text='quit program',command=exit)
b.pack()
eb.pack()

mainloop()













 
