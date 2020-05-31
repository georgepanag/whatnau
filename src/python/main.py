import eel
import calendar
import datetime
from User import User
import mysql.connector

#connect to database
mydb= mysql.connector.connect(
        host="localhost",
        user="whatnau",
        passwd="pasatempos64",
        database="whatnau")
usr1 = User(1)

#figure out todays date
today = datetime.datetime.today()
(c_year, c_month, c_day) = (today.year, today.month, today.day)

@eel.expose
def get_stats(year=c_year, month=c_month):
    days_iter = calendar.Calendar().itermonthdates(year, month)
    days_list = []
    all_events = usr1.showListEvents(mydb)
    user_events = []
    for day in days_iter:
        days_list.append(day)
        user_events.append(list(filter(lambda x:True if x[5].date() == day else False, all_events)))
                
    return {"days":days_list, "events":user_events}

print(get_stats())
print("---------------------")
eel.init("../web")
eel.start('month-view/month.html', size=(1000, 562))

mydb.close()
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
 
