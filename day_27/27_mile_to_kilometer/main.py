from tkinter import *

window = Tk()
window.title("Mile to Kilometer")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2,row=0)

label2 = Label(text="is equal to")
label2.grid(column=0,row=1)

label3 = Label(text="0")
label3.grid(column=1,row=1)

label4 = Label(text="Kilometers")
label4.grid(column=2,row=1)

def convert():
    miles = float(entry.get()) 
    km = round(1.609 * miles, 1)
    label3.config(text=str(km))

button = Button(text="Calculate", command=convert)
button.grid(column=1,row=2)

window.mainloop()