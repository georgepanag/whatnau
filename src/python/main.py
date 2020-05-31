import eel
import calendar
import datetime
from User import User
import mysql.connector

@eel.expose
def get_month_days():
    today = datetime.datetime.today()
    (c_year, c_month, c_day) = (today.year, today.month, today.day)
    days_iter = calendar.Calendar().itermonthdates(c_year, c_month)
    days = [(x.day,x.month) for x in days_iter]
    return days
   
mydb = mysql.connector.connect( host="localhost", user="whatnau", passwd="pasatempos64", database="whatnau" )
usr1 = User(1)
usr1.showListEvents()
#eel.init("../web")
#eel.start('month-view/month.html', size=(1000, 562))
