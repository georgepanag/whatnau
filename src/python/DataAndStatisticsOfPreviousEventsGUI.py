import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk



window = tk.Tk()
title_label = tk.Label(
    text="Display statistics",
    fg="white",
    bg="#1974D2",
    width=0,
    height=0
)
title_label.config(width=100)
title_label.config(font=("Courier", 30))

title_label.pack()

label1 = tk.Label(
    text="Please choose the kind of event:",
    fg="black",
    width=0,
    height=0
)

label1.place(x=40, y=50)

button1 = tk.Button(
    text="Concerts",
    width=12,
    height=2,
    bg="blue",
    fg="yellow",
)
button1.place(x=40, y=80)

button2 = tk.Button(
    text="Sporting events",
    width=12,
    height=2,
    bg="blue",
    fg="yellow",
)
button2.place(x=170, y=80)

button3 = tk.Button(
    text="Free of charge events",
    width=20,
    height=2,
    bg="blue",
    fg="yellow",
)
button3.place(x=300, y=80)

button4 = tk.Button(
    text="Other events",
    width=12,
    height=2,
    bg="blue",
    fg="yellow",
)
button4.place(x=494, y=80)

label2 = tk.Label(
    text="Please choose the region and the time period (dates) of the statistics for the event:",
    fg="black",
    width=0,
    height=0
)
label2.place(x=40, y=300)

label3 = tk.Label(
    text="From:",
    fg="black",
    width=0,
    height=0
)
label3.place(x=40, y=330)

label4 = tk.Label(
    text="Until:",
    fg="black",
    width=0,
    height=0
)
label4.place(x=430, y=330)

entry = tk.Entry()
entry.place(x=170, y=330)

entry2 = tk.Entry()
entry2.place(x=560, y=330)

label5 = tk.Label(
    text="Region:",
    fg="black",
    width=0,
    height=0
)
label5.place(x=40, y=550)

entry3 = tk.Entry()
entry3.place(x=170, y=550)

'''bg = PhotoImage(file="path to file")

# Show image using label
label1 = Label(window, image=bg)
label1.place(x=40, y=300)'''
window.configure(background='#CD7F32')

button5 = tk.Button(
    text="Back to the starting page",
    width=30,
    height=2,
    bg="blue",
    fg="yellow",
)
button5.place(x=930, y=600)

button6 = tk.Button(
    text="Submit preferences",
    width=32,
    height=2,
    bg="blue",
    fg="yellow",
)
button6.place(x=40, y=600)

window.mainloop()

