import mysql.connector


class User():

    def __init__(self,userID):
        self.userID=userID

    def searchBuddy(self,buddy_usrname):
        val=(buddy_usrname)
        mycursor = mydb.cursor()
        mycursor.execute("select * from _user where usrname = %s ",(val,))
        
        myresult = mycursor.fetchall()
        if len(myresult)!=0:
            print("buddy exist")
            return 1
        else:
            print("No such a buddy")
            return None
        #print(myresult)
        mycursor.close()
        mydb.close()


    #def friendReq(s
    def showListEvents(self,userID):
        events=[]
        val=(userID)
        mycursor = mydb.cursor()
        mycursor.execute("select _event.* from _event,_user where _user.userID =_event.userID and _user.userID= %s ",(val,))
        myresult = mycursor.fetchall()
        for coloumns in myresult:
            for values in coloumns:
                events.append(values)
                #print(values)
        #print(events)
        return events
        mycursor.close()
        mydb.close()
    
    def showUrgEvents(self,userID):
        urg_events=[]
        val=(userID)
        mycursor = mydb.cursor()
        mycursor.execute("select _event.* from _event,_user where _user.userID =_event.userID and _event.importance='HIGH' and _user.userID= %s ",(val,))
        myresult = mycursor.fetchall()
        for coloumns in myresult:
            for values in coloumns:
                urg_events.append(values)
                #print(values)
        #print(urg_events)
        return urg_events
        mycursor.close()
        mydb.close()


mydb= mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="pasatempo64",
        database="whatnau")

user1=User(2)
user1.showUrgEvents(2)
