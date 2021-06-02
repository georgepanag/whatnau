import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window = tk.Tk()
title_label = tk.Label(
    text="Menu events",
    fg="white",
    bg="#1974D2",
    width=0,
    height=0
)
title_label.config(width=100)
title_label.config(font=("Courier", 30))

title_label.pack()

label1 = tk.Label(
    text="Choose one of the following proposed for you events:",
    fg="black",
    width=0,
    height=0
)

label1.place(x=40, y=50)

button1 = tk.Button(
    text="Concert of Scorpions in Patras",
    width=32,
    height=2,
    bg="blue",
    fg="yellow",
)
button1.place(x=40, y=80)

button2 = tk.Button(
    text="Footall match Olympiacos-Panathinaikos in Athens",
    width=50,
    height=2,
    bg="blue",
    fg="yellow",
)
button2.place(x=40, y=160)

button3 = tk.Button(
    text=" Book fair in Kalamata",
    width=32,
    height=2,
    bg="blue",
    fg="yellow",
)
button3.place(x=40, y=240)

label2 = tk.Label(
    text="Search for an event of your choice:",
    fg="black",
    width=0,
    height=0
)

label2.place(x=40, y=400)

button4 = tk.Button(
    text="Search event",
    width=32,
    height=2,
    bg="blue",
    fg="yellow",
)
button4.place(x=40, y=480)

button5 = tk.Button(
    text="Back to your starting page",
    width=32,
    height=2,
    bg="blue",
    fg="yellow",
)
button5.place(x=930, y=600)

window.configure(background='#C0E8D5')

window.mainloop()