import mysql.connector


#mydb=mysql.connector.connect(host="localhost", user="root", passwd="password", database="whatnau") 


class Organiser():
    

    def __init__(self, promotedID):
        self.promotedID=promotedID


    #for uploading a new event
    def uploadEvent(self, descr, category, entrance_value, start_date, end_date, target_aud)
        val=(self.promotedID, descr, category, entrance_value, start_date, end_date, target_aud)
        mycursor = mydb.cursor()            
        mycursor.execute("insert_into promoted_event(promotedID, descr, category, entrance_value, start_date, end_date, target_aud) values (%s, %s, %s, %s, %s, %s, %s)", val)
        mydb.commit()
        print(mycursor.rowcount, "new event uploaded")
        mycursor.close()

    #for changing events information
    def AlterEvent(self, onefield, changing):
        if onefield == "descr":
            self.setter(onefield, changing)
        if onefield == "category":
            self.setter(onefield, changing)
        if onefield == "entrance_value":
            self.setter(onefield, changing)
        if onefield == "target_aud":
            self.setter(onefield, changing)
        if onefield == "start_date":
            self.setter(onefield, changing)
        if onefield == "end_date":
            self.setter(onefield, changing)
    
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
        
        
        
