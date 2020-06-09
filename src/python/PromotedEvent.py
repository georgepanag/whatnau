import mysql.connector
import Event
from Event import *


class PromotedEvent(Event):

    def __init__(self,promotedID,userID,descr="No descr",category="undefined",entrance_value=0,target_aud="to all",start_date=None,end_date=None,location=None):
        
        self.promotedID=promotedID
        self.userID=userID
        self.descr=descr
        self.category=category
        self.entrance_value=entrance_value
        self.target_aud=target_aud
        self.start_date=start_date
        self.end_date=end_date
        self.location=location

    

    def E_getter(self,col,mydb):
        get_list=[]
        c=str(col)
        mycursor1 = mydb.cursor()
        mycursor1.execute("select " + c + " from promoted_event where promotedID="+str(self.promotedID))
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
        

        val=(str(modification))
        c=str(col)
        mycursor = mydb.cursor()
        mycursor.execute("update promoted_event set "+ c +" = %s where promotedID="+str(self.promotedID),(val,))
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        mycursor.close()
    
    def AlterEvent(self,mode,change):
        
        if mode=="descr":               
            self.P_setter(mode,change)
            
        if mode =="category":
            self.P_setter(mode,change)
                        
        if mode =="entrance_value":
            self.P_setter(mode,change)

        if mode =="target_aud":
            self.P_setter(mode,change)    

        if mode=="start_date":
            self.P_setter(mode,change)
    
        if mode=="end_date":
            self.P_setter(mode,change)

        if mode=="location":
            self.P_setter(mode,change)

         
    def deletePromotedEvent(self,mydb):
        val=(str(self.promotedID))
        mycursor = mydb.cursor()
        mycursor.execute("delete from promoted_event where promotedID = %s",(val,))
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        mycursor.close()


    

#for testing
mydb= mysql.connector.connect(
           host="localhost",
            user="root",
            passwd="pasatempo64",
            database="whatnau")
'''except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
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

e=PromotedEvent(1,1)
e.E_getter("descr",mydb)
#E_getter <-Event

mydb.close()     
