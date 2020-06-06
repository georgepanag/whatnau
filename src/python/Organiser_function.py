def send_to_fans(self,userID,mydb):
        val =userID

        mycursor = mydb.cursor()
        mycursor.execute("select interests  from _user where userID=%s ",(val,))
        
        myresult = mycursor.fetchone()
        print (str(myresult[0])) #just checking the result
        
        mycursor.close()


        mycursor2 = mydb.cursor()
        mycursor2.execute("select category  from promoted_event where userID=%s ",(val,))
        
        myresult2 = mycursor2.fetchone()
        print (str(myresult2[0])) #just checking the result
        return str(myresult)
        return str(myresult2)
        mycursor2.close()

        if (myresult)==(myresult2):
            mycursor3 = mydb.cursor()
        
            sql="update promoted_event set userID = %s"
            variable=(val, userID)
            mycursor3.execute(sql, variable)
       
        
            mydb.commit()
            print(mycursor3.rowcount, "record(s) affected")
            
        
            
        
        
        
        
        mycursor2.close()

        
