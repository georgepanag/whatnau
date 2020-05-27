import eel
import calendar
import datetime

@eel.expose
def get_month_days():
    today = datetime.datetime.today()
    (c_year, c_month, c_day) = (today.year, today.month, today.day)
    days_iter = calendar.Calendar().itermonthdates(c_year, c_month)
    days = [(x.day,x.month) for x in days_iter]
    return {"days_list": days,"month":c_month, "day": c_day}
   
eel.init("../web")
eel.start('month-view/month.html', size=(1000, 562))
