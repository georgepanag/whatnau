import mysql.connector




class Event():
    
    

    def __init__(self,eventID,):#,importance,descr,_type,time_start,time_end,is_shared):
        self.eventID=eventID
        
    def get_descr(self):
        mycursor = mydb.cursor()
        mycursor.execute("select descr from _event where userID="+str(self.eventID))
        myresult = mycursor.fetchall()
        for coloumn in myresult:
            for value in coloumn:
                return str(value)
                #print(str(value))
        #print(myresult)
        mycursor.close()
        mydb.close()
    

    def set_descr(self,my_descr):
        

        val=(str(my_descr),'''eventID goes here''')
        mycursor = mydb.cursor()
        mycursor.execute("update _event set descr= %s where _event.userID=%s",val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
       
        mycursor.close()
        mydb.close()

    

    
    



mydb= mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="pasatempo64",
        database="whatnau")
a=Event(4)
a.get_descr()
a.set_descr("basketball!")
a.get_descr()
        
