# Import tkinter
from tkinter import *

# Create the root window
root = Tk()
root.geometry('650x340')
root.title("Whatnau")

# Create the label on top
lbl=Label(text="Choose an event and the type of rating you wish to answer", fg='black', bg='#C0E9F9', font=("Helvetica", 16))

# Create a listbox
listbox = Listbox(root, width=40, height=15)

# Inserting the listbox items with random values
# Checking
listbox.insert(1, "Scorpions concert")
listbox.insert(2, "Olympiacos-Panathinaikos")
listbox.insert(3, "Book presentation")
listbox.insert(4, "Playing basketball with friends")
listbox.insert(5, "Cinema")
listbox.insert(6, 'Go out with friends')

# Create the 2 buttons
btn1 = Button(root, text='Extended rating')
btn2 = Button(root, text='Simple rating')

# Placing the button, listbox and label
btn1.pack(side='bottom')
btn2.pack(side='bottom')
listbox.pack(side='bottom')
lbl.pack(side='top')

# Background colour
root.configure(background='#C0E8D5')


root.mainloop()

