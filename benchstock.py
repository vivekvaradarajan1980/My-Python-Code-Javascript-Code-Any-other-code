from tkinter import *
import win32com.client as win32
import os
from tkinter import messagebox
import datetime

from  pandas  import  *

excel=win32.Dispatch('Excel.Application')
excel.Visible = 0
excel.DisplayAlerts=False

def IntoNSN(anynum):
    x = "%013d" % int(anynum)
    result = "{0}-{1}-{2}-{3}".format(x[:4], x[4:6], x[6:9], x[9:])
    return result


def excelmodify(data):
    if (os.path.exists("C:\Transfers\Toolcatalog.xls") == False):
        wb = excel.Workbooks.Add()

        ws = wb.ActiveSheet
    else:
        wb = excel.Workbooks.Open("C:\Transfers\Toolcatalog.xls")
    try:
        ws = wb.Sheets(sheetname.get())

    except:
        ws = wb.Worksheets.Add()
        ws.Name = sheetname.get()
    global readin, readout

    nb = 2

    flag = False
    update = True

    while (ws.Cells(nb, 2).Value != None and ws.Cells(nb, 2).Value != data[0][1]):
        nb = nb + 1

    if (ws.Cells(nb, 2).Value == data[0][1]):

        root.withdraw()

        flag = messagebox.askyesno('Entry exist at ' + ws.Cells(nb, 1).Text + ' yes to delete or no to update')

        if (flag == True):

            ws.Rows(nb).Delete()
            wb.SaveAs("C:\Transfers\Toolcatalog.xls")
        else:
            update = messagebox.askyesno('Update entry')

    if (flag == False and update == True):  # ask if entry needs to be updated for duplicate entry
        if (nb == 2):
            readin = sorted(tuple(data), key=lambda x: (x[1]))
        else:

            readout = ws.Range("A2:F" + str(nb - 1)).Value

            readin = sorted(readout + tuple(data), key=lambda x: (x[1]))

        ws.Range("A2:F" + str(len(readin) + 1)).Value = readin

        ws.Columns.AutoFit()
    wb.SaveAs("C:\Transfers\Toolcatalog.xls")

    root.deiconify()


alldata = []


def adddata():
    data = []
    data.append(tuple([boxnum.get(), IntoNSN(nsn.get()), partname.get(), signedby.get(), var1.get(),
                       datetime.datetime.now().date().isoformat()]))

    partname.delete(0, END)
    nsn.delete(0, END)
    boxnum.delete(0, END)
    var1.set(0)
    alldata.append(data)

    excelmodify(data)


def quitfun():
    root.destroy()
    #    wb.Close(SaveChanges=0) #to avoid prompt
    excel.Quit()


# optional entries are Toolname and Tool location, if signed out type in persons' name and tool ID
root = Tk()
var1 = IntVar()
Label(root, text="Tool ID/NSN", fg='blue', font=15).grid(row=0, column=0)
Label(root, text="Toolname", fg='blue', font=25).grid(row=0, column=2)
Label(root, text="Tool location", fg='blue', font=15).grid(row=1, column=0)
Label(root, text="Signed out by", fg='blue', font=15).grid(row=1, column=2)
signedout = Checkbutton(root, text="Signed out", fg='blue', font=15, variable=var1)
signedout.grid(row=3, column=3)
Label(root, text="Vinmar  name", fg='blue', font=15).grid(row=2)
nsn = Entry(root, width=15)
partname = Entry(root, width=14)
boxnum = Entry(root, width=10)
signedby = Entry(root, width=30)
sheetname = Entry(root, width=14)
partname.grid(row=0, column=3)
nsn.grid(row=0, column=1)
boxnum.grid(row=1, column=1)
signedby.grid(row=1, column=3)
sheetname.grid(row=2, column=1)
b = Button(root, text='Add', font=15, fg='green', command=adddata)
b.grid(row=3)
b1 = Button(root, text='quit', font=15, fg='red', command=quitfun)
b1.grid(row=3, column=2)

mainloop()
