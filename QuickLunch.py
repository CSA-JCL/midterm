from tkinter import ttk
from tkinter import *

window = Tk()
window.title("Quick Lunch")
window.geometry('500x500')

window2 = Toplevel()
window2.title('About')
window2.geometry("400x200")

window3 = Toplevel()
window3.title('Instructions')
window3.geometry("400x200")

radio = StringVar()


def reset_all():
    radio.set(' ')

menubar = Menu(window)
menubar2 = Menu(window2)
menubar3 = Menu(window3)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="About", command=window2.deiconify)
filemenu.add_command(label="Instructions", command=window3.deiconify)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Menu", menu=filemenu)
window.config(menu=menubar)

filemenu2 = Menu(menubar2, tearoff=0)

filemenu2.add_command(label="Exit", command=window2.withdraw)
menubar2.add_cascade(label="Menu", menu=filemenu2)
window2.config(menu=menubar2)

filemenu3 = Menu(menubar3, tearoff=0)

filemenu3.add_command(label="Exit", command=window3.withdraw)
menubar3.add_cascade(label="Menu", menu=filemenu3)
window3.config(menu=menubar3)


madeby = Label(window2,text= "This Program was made by Jack Lawrence").grid(column = 0, row = 0)
version = Label(window2,text= "Version 1.0").grid(column= 0, row= 0,sticky = S)

ins = Label(window3, text="Input what you want to order, the day, and your ID").grid(column = 0, row = 0, padx=50)
drink = ['Drink','Soda [$1]','Tea [$1]','Milk [$0.75]','Juice [$1.25]','Bottled Water [$1]']


Label(window,text=drink[0]).grid(row=0,sticky=W)
Radiobutton(window, text=drink[1], variable =radio, value = drink[1]).grid(row=1,columnspan = 5, sticky=W)
Radiobutton(window, text=drink[2], variable =radio, value = drink[2]).grid(row=2,sticky=W)
Radiobutton(window, text=drink[3], variable =radio, value = drink[3]).grid(row=3,sticky=W)
Radiobutton(window, text=drink[4], variable =radio, value = drink[4]).grid(row=4,sticky=W)
Radiobutton(window, text=drink[5], variable =radio, value = drink[5]).grid(row=5,sticky=W)

l = Listbox(window, height=6, width = 45)
l.grid(column=3, row=1, columnspan = 10, rowspan = 10, sticky=E)
l.bind("<<ListboxSelect>>")
listlable = ttk.Label(window, text="Entrees")
listlable.grid(column=3, row=0,sticky=W)
for item in ["Sandwich [$3]", "Pizza [$4]", "Chicken Nuggets [$3.75]", "Chicken [$4]","Tofu[$15]","Gluten/Soy/Shellfish Free Clam Chowder [$20]"]:
    l.insert(END, item)

paymentoptions = ("Credit","Cash","Check")
choices = ttk.Combobox(window,state='readonly',values=paymentoptions).grid(row=8,column= 0, sticky= W)

ID = Entry(window).grid(row=8, column = 3)
IDlable = Label(window, text="Employee ID:").grid(padx =10, row=8, column= 2)

days = Spinbox(window, state='readonly',values=("Monday", "Tuesday", "Wednesday", "Thursday","Friday","Saturday","Sunday")).grid(row=7, column = 0, sticky=W)

calc = Button(window, text= "CALCULATE").grid( row= 9, column = 0, sticky= W)
checkout = Button(window, text= "CHECKOUT").grid( row= 10, column = 0, sticky= W)
reset_all()
window3.withdraw()
window2.withdraw()
window.mainloop()
