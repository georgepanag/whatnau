import eel
import calendar
import datetime
from User import User
import mysql.connector


mydb= mysql.connector.connect(
        host="localhost",
        user="whatnau",
        passwd="pasatempos64",
        database="whatnau")

@eel.expose
def get_month_days():
    today = datetime.datetime.today()
    (c_year, c_month, c_day) = (today.year, today.month, today.day)
    days_iter = calendar.Calendar().itermonthdates(c_year, c_month)
    days = [(x.day,x.month) for x in days_iter]
    return days
   

usr1 = User(1)
print(usr1.showListEvents(mydb))
mydb.close()
#eel.init("../web")
#eel.start('month-view/month.html', size=(1000, 562))

def userExists(user_email,user_pass):
    val=(user_email,user_pass)
    mycursor = mydb.cursor()
    mycursor.execute("select userID from _user where email= %s and pass= %s ",val)
    myresult = mycursor.fetchall()
    if len(myresult)!=0:
        print("Welcome user")
        #print(myresult)
        return True
    else:
        print("Invalid password or email address OR user doesn't exist\nplease try again")
        #print(myresult)
        return False
 
