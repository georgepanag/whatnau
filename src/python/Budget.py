from tkinter import *

window=Tk()

btn=Button(window, text="New Transaction", fg='black')
btn.place(x=400, y=180)

btn=Button(window, text="History/Graph of past transactions", fg='black')
btn.place(x=352, y=220)

btn=Button(window, text="Go Back", fg='black')
btn.place(x=10, y=10)

lbl=Label(window, text="Budget", fg='black', bg='#C0E8D5', font=("Helvetica", 20))
lbl.place(x=403, y=50)

lbl=Label(window, text="Here you can do a transaction or check your past done transactions", fg='black', bg='#C0E8D5', font=("Helvetica", 14))
lbl.place(x=155, y=105)


window.title('Whatnau')
window.geometry("900x410+10+10")

window.configure(background='#C0E8D5')

window.mainloop()
