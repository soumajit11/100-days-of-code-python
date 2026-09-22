from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
#Label
my_label = Label(text = "I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side = "left", expand=True)

my_label["text"] = "New Text"
my_label.config(text="New Text 2")

#button
def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())
button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry
input = Entry(width=10)
input.pack()
print(input.get())