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

#creare user object and download it's events
usr1 = User(1)
usr1.getEventsFromDB(mydb)

#figure out todays date
today = datetime.datetime.today()
(c_year, c_month, c_day) = (today.year, today.month, today.day)

def datetime_to_tuple(datetime):
    x = (datetime.year,datetime.month,datetime.day,datetime.hour,datetime.minute,datetime.second)
    return x

def make_js_complient(variable):
    if isinstance(variable,datetime.datetime):
        return datetime_to_tuple(variable)
    elif isinstance(variable,(set,list)): 
        return [make_js_complient(x) for x in variable]
    elif isinstance(variable,dict):
        return {k : make_js_complient(v) for k, v in variable.items()}
    else:
        return variable



@eel.expose
def get_stats(year=c_year, month=c_month):
    days_iter = calendar.Calendar().itermonthdates(year, month)
    days_list = []
    events_list = {} 
    all_events = usr1.events
    for day in days_iter:
        events_list.update( {day.strftime("%Y,%-m,%-d") : len(list(filter(lambda x :True if x.start_date.date() == day else False, all_events))) })
        days_list.append((day.year,day.month,day.day))

    return {"days": days_list, "user_events" : events_list}

def get_day_events(year=c_year, month=c_month, day=c_day):
    day_start = datetime.datetime(year,month,day)
    day_events = []
    for evnt in usr1.events:
        if evnt.start_date <= day_start and day_start <= evnt.end_date:
            day_start.append(evnt);


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

 #-------------------------------
for e in usr1.events:
     print(e.start_date.date())

eel.init("../web")
eel.start('month-view/month.html', size=(1000, 562))


mydb.close()


