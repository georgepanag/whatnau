def get_promoted_events(self,category,mydb):
        val =(category)
        #val2=category
        mycursor = mydb.cursor()
        
        mycursor.execute("select * from promoted_event where target_aud= 'only fans' and category LIKE %s",(val,))
        
        
        myresult = mycursor.fetchall()
        #print (myresult)
        return (myresult)
        mycursor.close()
