import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window = tk.Tk()
title_label = tk.Label(
    text="Search for the event of your choice!",
    fg="white",
    bg="black",
    width=0,
    height=0
)
title_label.config(width=100)
title_label.config(font=("Courier", 30))

title_label.pack()

label1 = tk.Label(
    text="Complete the following fields:",
    fg="black",
    width=0,
    height=0
)

label1.config(font=("Courier", 17))
label1.place(x=40, y=50)

label2 = tk.Label(
    text="Type region:",
    fg="black",
    width=0,
    height=0
)

label2.place(x=40, y=80)


entry = tk.Entry()
entry.place(x=180, y=80)

label3 = tk.Label(
    text="Select hour:",
    fg="black",
    width=0,
    height=0
)

label3.place(x=40, y=130)

class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.hourstr=tk.StringVar(self,'10')
        self.hour = tk.Spinbox(self,from_=0,to=23,wrap=True,textvariable=self.hourstr,width=2,state="readonly")
        self.minstr=tk.StringVar(self,'30')
        self.minstr.trace("w",self.trace_var)
        self.last_value = ""
        self.min = tk.Spinbox(self,from_=0,to=59,wrap=True,textvariable=self.minstr,width=2,state="readonly")
        self.hour.grid()
        self.min.grid(row=0,column=1)

    def trace_var(self,*args):
        if self.last_value == "59" and self.minstr.get() == "0":
            self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() !="23" else 0)
        self.last_value = self.minstr.get()


App(window).place(x=180,y=130)

label4 = tk.Label(
    text="Select category:",
    fg="black",
    width=0,
    height=0
)

label4.place(x=40, y=180)



OPTIONS = [
"Concerts",
"Sporting events",
"Free of charge events",
"Other events"
]


variable = StringVar(window)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(window, variable, *OPTIONS)
w.place(x=180, y=180)

label5 = tk.Label(
    text="Grade of popularity:",
    fg="black",
    width=0,
    height=0
)

label5.place(x=40, y=230)


OPTIONS = [
"1",
"2",
"3",
"4",
"5"
]


variable2 = StringVar(window)
variable2.set(OPTIONS[0]) # default value

w = OptionMenu(window, variable2, *OPTIONS)
w.place(x=180, y=230)

label6 = tk.Label(
    text="Entrance fee (euros):",
    fg="black",
    width=0,
    height=0
)

label6.place(x=40, y=280)


entry2 = tk.Entry()
entry2.place(x=180, y=280)

button1 = tk.Button(
    text="Submit preferences",
    width=32,
    height=2,
    bg="blue",
    fg="yellow",
    command= quit
)
button1.place(x=40, y=600)

button2 = tk.Button(
    text="Back to the events menu",
    width=30,
    height=2,
    bg="blue",
    fg="yellow",
)
button2.place(x=930, y=600)

window.configure(background='#C0E8D5')

window.mainloop()
