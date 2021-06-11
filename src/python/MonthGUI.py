import tkinter as tk
import calendar as cal
from datetime import date

# retrieve current date info
today = date.today()
year = today.year
month = today.month
day = today.day
C = cal.Calendar()
days_list = C.monthdatescalendar(year,month)

window = tk.Tk()

top_bar = tk.Frame(master=window)
date_label = tk.Label(
        master=top_bar, 
        text=today.strftime("%a, %d %b %Y"),
        font=("Arial",50) 
        )
date_label.pack()
top_bar.pack()

main_frame= tk.Frame(master=window)

rect_side=100
i = 0;
while i < 35:
    loop_week = i//7
    loop_day = i%7
    loop_date = days_list[loop_week][loop_day]
    text = loop_date.strftime("%A")

    frame = tk.Frame(
            main_frame,
            width=rect_side,
            height=rect_side,
            borderwidth=1,
            relief="solid"
            )
    if loop_date.month != month:
        frame.configure(background='gray')
    if loop_date.month == month and loop_date.day == day:
        frame.configure(background='cyan')
    frame.pack_propagate(0)

    label_1 = tk.Label(
            master = frame,
            text = text
            ).pack()
    
    label_2 = tk.Label(
            master = frame,
            text = loop_date.day
            ).pack()

    frame.grid(row=loop_week,column=loop_day)

    i = i+1;

main_frame.pack()

window.mainloop()



