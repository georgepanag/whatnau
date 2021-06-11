import tkinter as tk
import calendar as cal
from datetime import date

# retrieve current date info
today = date.today()
year = today.year
month = today.month
C = cal.Calendar()
days_list = C.monthdatescalendar(year,month)

window = tk.Tk()

day_frames=[]

i = 0;
while i < 35:
    loop_week=i//7
    loop_day=i%7 
    #print(loop_week)
    #print(loop_day)
    #print(i)
    #print("-------")
    day_frames.append(
            tk.Frame()
            tk.Label(
                text=days_list[loop_week][loop_day].strftime("%A"),
                width=10,
                height=10,
                borderwidth=1,
                relief="solid"
                ).grid(
                    row=loop_week,
                    column=loop_day
                    )
            )
    i = i+1;

window.mainloop()



