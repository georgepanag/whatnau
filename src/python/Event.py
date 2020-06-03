import mysql.connector




class Event():
    
    

    def __init__(self,eventID,descr="No descr",_type="undefined",importance="HIGH",start_date=None,end_date=None,shared="NO"):#,importance,descr,_type,time_start,time_end,is_shared):
        self.eventID=eventID
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
    def deleteEvent(self,mydb):
        val=(str(self.eventID))
        mycursor = mydb.cursor()
        mycursor.execute("delete from _event where eventID = %s",(val,))
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        mycursor.close()


