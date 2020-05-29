import mysql.connector




class Event():
    
    

    def __init__(self,eventID):#,importance,descr,_type,time_start,time_end,is_shared):
        self.eventID=eventID
        '''self.importance="HIGH"#importance
        self.descr="No descr"#descr
        self._type="undefined"#_type
        self.start_date=None#"0000-00-00 00:00:00"#time_start
        self._end_date=None#"0000-00-00 00:00:00"#time_end
        self.shared="NO"#shared'''

                
    def E_getter(self,col):
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
    

   


    def E_setter(self,col,modification):
        

        val=(str(modification))#,
        c=str(col)
        mycursor = mydb.cursor()
        mycursor.execute("update _event set "+ c +" = %s where eventID="+str(self.eventID),(val,))
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        mycursor.close()
    
    def AlterEvent(self,mode,change): #mode can be importance,descr,_type,time_start,time_end,is_shared except eventID
        if mode=="descr":              #change is the new modificatio a.k.a update on a table 
            self.setter(mode,change)
            
        if mode =="_type":
            self.setter(mode,change)
                        
        if mode =="shared":
            self.setter(mode,change)

        if mode =="importance":
            self.setter(mode,change)    

        if mode=="start_date":
            self.setter(mode,change)
    
        if mode=="_end_date":
            self.setter(mode,change)

        #mporei kai ston User 
    def deleteEvent(self):
        val=(str(self.eventID))
        mycursor = mydb.cursor()
        mycursor.execute("delete from _event where eventID = %s",(val,))
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        mycursor.close()


    

#for testing
mydb= mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="whatnau")
e=Event(1,importance="LOW")
print(e.importance)
'''
y="2020"
m="05"
d="8"
h="16"
mi="45"
s="00"

from datetime import datetime
#converts to datetime
req_date = datetime(year=int(y),
                month=int(m),
                day=int(d),
                hour=int(h),
                minute=int(mi),
                second=int(s))



a=Event(1)
a.getter("descr")
'''
mydb.close()     

