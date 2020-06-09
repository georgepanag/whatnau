import mysql.connector


#mydb=mysql.connector.connect(host="localhost", user="root", passwd="password", database="whatnau") 


class Organiser():
    

    def __init__(self, promotedID,userID):
        self.promotedID=promotedID
        self.userID=userID
        promoteds=[]

    def getPromotedFromDB(self, mydb):
        val=(str(self.userID))
        promoteds=[]
        mycursor = mydb.cursor()
        mycursor.execute("select * from promoted_event where userID = %s ",(val,))
        myresult = mycursor.fetchall()
        
        for evnt in myresult:
            self.promoteds.append(PromotedEvent(evnt[0],evnt[1],evnt[2],evnt[3],evnt[4],evnt[5],evnt[6],evnt[7],evnt[8]))
        mycursor.close()
    
        
        

    #for uploading a new event
    def uploadEvent(self, descr, category, entrance_value, start_date, end_date, target_aud):
        val=(self.promotedID, descr, category, entrance_value, start_date, end_date, target_aud)
        mycursor = mydb.cursor()            
        mycursor.execute("insert_into promoted_event(promotedID, descr, category, entrance_value, start_date, end_date, target_aud) values (%s, %s, %s, %s, %s, %s, %s)", val)
        mydb.commit()
        print(mycursor.rowcount, "new event uploaded")
        mycursor.close()


    #for deleting an existing uploading event
    def deleteUploadingEvent(self):
        val=(str(self.promotedID))
        mycursor=mydb.cursor()
        mycursor.execute("delete from promoted_event where promotedID=%s", (val,))
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
        mycursor.close()




    #finds the sum of users who have the uploading event on their list
    def symmetexontesEvent(self):
        mycursor = mydb.cursor()
        mycursor.execute=("select COUNT(userID) from participants where promotedID=%s")
        myresult = mycursor.fetchone()
        mycursor.close()
        
        
        
