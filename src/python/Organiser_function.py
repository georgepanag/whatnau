def send_to_fans(self,userID,mydb):
        val =userID
        
        mycursor = mydb.cursor()
        
        mycursor.execute("select interests  from _user")
        
        myresult = mycursor.fetchall()
        #for x in myresult:
            #print(x) #just checking the result
            
       
        print("________________________")

        mycursor2 = mydb.cursor()
        mycursor2.execute("select category  from promoted_event")
        
        myresult2 = mycursor2.fetchall()
        #for y in myresult2:
            #print(y) #just checking the result
        
        for x in myresult:
            for y in myresult2:
        
                if (x)==(y):
                    mycursor3 = mydb.cursor()
                    
                    sql="update promoted_event set userID=%s "
                    variable=(val)
                    mycursor3.execute(sql, variable)
               
                
                    mydb.commit()
                    print(mycursor3.rowcount, "record(s) affected")

                    mycursor3.close()
                else:
                    print("The Elements don't match each other")
        mycursor.close()    
        mycursor2.close()
        
         
        
       #mydb.close()
        
