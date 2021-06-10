import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root123!",
    database="whatnau")


class Event():
    
    

    def __init__(self,eventID,userID,descr="No descr",_type="undefined",importance="HIGH",start_date=None,end_date=None,shared="NO"):#,importance,descr,_type,time_start,time_end,is_shared):
        self.eventID=eventID
        self.userID=userID
        self.descr=descr
        self._type=_type
        self.importance=importance
        self.start_date=start_date
        self._end_date=end_date
        self.shared=shared

                
    def E_getter(self,col,mydb):
        get_list=[]
        c=str(col)
        mycursor1 = mydb.cursor()
        mycursor1.execute("select " + c + " from _event where eventID="+str(self.eventID))
        myresult = mycursor1.fetchall()
        for coloumn in myresult:
            for value in coloumn:
                get_list.append(value)
                print(get_list)
                return str(get_list)
        #print(myresult)
        mycursor1.close()
        #mydb.close()
    

   


    def E_setter(self,col,modification,mydb):
        

        val=(str(modification))#,
        c=str(col)
        mycursor = mydb.cursor()
        mycursor.execute("update _event set "+ c +" = %s where eventID="+str(self.eventID),(val,))
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        mycursor.close()
    
    def AlterEvent(self,mode,change): #mode can be importance,descr,_type,time_start,time_end,is_shared except eventID
        if mode=="descr":              #change is the new modificatio a.k.a update on a table 
            self.E_setter(mode,change)
            
        if mode =="_type":
            self.E_setter(mode,change)
                        
        if mode =="shared":
            self.E_setter(mode,change)

        if mode =="importance":
            self.E_setter(mode,change)    

        if mode=="start_date":
            self.E_setter(mode,change)
    
        if mode=="_end_date":
            self.E_setter(mode,change)

        #mporei kai ston User 
        
    def deleteEvent(self,mydb):
        val=(str(self.eventID))
        mycursor = mydb.cursor()
        mycursor.execute("delete from _event where eventID = %s",(val,))
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        mycursor.close()
        
    def ShowPublicEvents(self, userID, mydb):
        val = userID
        mycursor = mydb.cursor()
        mycursor.execute("select eventID from _event ", (val,))

        myresult = mycursor.fetchone()

        mycursor.close()

    def SearchEvent(self, userID, event_ID, region, event_hour, category, grade_of_popularity, entrance_fee, mydb):
        val1 = userID
        val2 = event_ID
        val3 = region
        val4 = event_hour
        val5 = category
        val6 = grade_of_popularity
        val7 = entrance_fee

        mycursor = mydb.cursor()

        mycursor.execute("select userID from _event where userID=%s ", (val1,))
        mycursor.execute("select event_ID from _event where userID=%s ", (val2,))
        mycursor.execute("select region from _event where userID=%s ", (val3,))
        mycursor.execute("select event_hour from _event where userID=%s ", (val4,))
        mycursor.execute("select category from _event where userID=%s ", (val5,))
        mycursor.execute("select grade_of_popularity from _event where userID=%s ", (val6,))
        mycursor.execute("select entrance_fee from _event where userID=%s ", (val7,))

        myresult = mycursor.fetchone()

        mycursor.close()

    def RetrieveUsersWithCommonInterests(self, userID,_type):
        val1 = userID
        val2 = _type
        mycursor = mydb.cursor()
        sql = 'select userID from _event where _type=%s and _event.userID._type=%s ', (val2,val2,)
        mycursor.execute(sql)

        myresult = mycursor.fetchall()


        mycursor.close()


#Event1 = Event(1)
     


