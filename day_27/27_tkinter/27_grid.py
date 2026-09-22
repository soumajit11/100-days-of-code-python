from tkinter import *
#pack and grid cant be used together in a program 
window = Tk()
window.title("Grid")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(column=0,row=0)
label.config(padx=10,pady=10)

button = Button(text="Click Me")
button.grid(column=1,row=1)

button2 = Button(text="New")
button2.grid(column=2,row=0)

entry = Entry(width=10)
entry.insert(END, string="INPUT!")
entry.grid(column=3,row=2)

window.mainloop()