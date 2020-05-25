import mysql.connector




class Event():
    
    

    def __init__(self,eventID):#,importance,descr,_type,time_start,time_end,is_shared):
        self.eventID=eventID
        '''self.importance=None#importance
        self.descr=None#descr
        self._type=None#_type
        self.time_start=None#time_start
        self.time_end=None#time_end
        self.shared=None#shared'''

                
    def getter(self,col):
        get_list=[]
        c=str(col)
        mycursor1 = mydb.cursor()
        mycursor1.execute("select " + c + " from _event where userID="+str(self.eventID))
        myresult = mycursor1.fetchall()
        for coloumn in myresult:
            for value in coloumn:
                get_list.append(value)
                #return str(value)
                print(value)
        #print(myresult)
        mycursor1.close()
        #mydb.close()
    

   


    def setter(self,col,modification):
        

        val=(str(modification))#,
        c=str(col)
        mycursor = mydb.cursor()
        mycursor.execute("update _event set "+ c +" = %s where eventID="+str(self.eventID),(val,))
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        mycursor.close()
    
    def modifyEvent(self,mode,change): #mode can be importance,descr,_type,time_start,time_end,is_shared except eventID
        if mode=="descr":
            self.setter(mode,change)
            #print(self.setter(mode,change))
        if mode =="_type":
            self.setter(mode,change)
                        
        if mode =="shared":
            self.setter(mode,change)

        if mode =="importance":
            self.setter(mode,change)    

        if mode=="start_date":
            self.setter(mode,change)
    
        if mode=="end_date":
            self.setter(mode,change)

''' for testing
mydb= mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="pasatempo64",
        database="whatnau")
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

mydb.close()     
'''
