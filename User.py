import mysql.connector


class User():

    def __init__(self,userID):
        self.userID=userID
        '''
        self.email=space
        self.usrname=usrname
        self.interest=interest
        self.gender=interest
        self._type=_type
        self.job=job
        self.corporation=corporation
        self.space=space'''
        


        
    


    #def friendReq(s
    def showListEvents(self,userID):
        events=[]
        val=(userID)
        mycursor = mydb.cursor()
        mycursor.execute("select _event.* from _event,_user where _user.userID =_event.userID and _user.userID= %s ",(val,))
        myresult = mycursor.fetchall()
        for coloumn in myresult:
            for values in coloumn:
                events.append(values)
                #print(values)
        print(events)
        return events
        mycursor.close()
        #mydb.close()
    
    def showUrgEvents(self,userID):
        urg_events=[]
        val=(userID)
        mycursor = mydb.cursor()
        mycursor.execute("select _event.* from _event,_user where _user.userID =_event.userID and _event.importance='HIGH' and _user.userID= %s ",(val,))
        myresult = mycursor.fetchall()
        for coloumn in myresult:
            for values in coloumn:
                urg_events.append(values)
                #print(values)
        #print(urg_events)
        return urg_events
        mycursor.close()
        #mydb.close()
        
    def addEvent(self,descr,_type,importance,start_date,_end_date,shared): #To userID to pairnei automata apo to User antikeimeno
        val=(self.userID,descr,_type,importance,start_date,_end_date,shared)
        mycursor = mydb.cursor()
        mycursor.execute("insert into _event(userID,descr,_type,importance,start_date,_end_date,shared) values (%s, %s, %s, %s, %s, %s, %s)",val)
        mydb.commit()               
        print(mycursor.rowcount, "event created")
        mycursor.close()


    def searchBuddy(self,buddy_usrname):
        val=(buddy_usrname)
        mycursor = mydb.cursor()
        mycursor.execute("select * from _user where usrname = %s ",(val,))
        
        myresult = mycursor.fetchall()
        if len(myresult)!=0:
            #print("buddy exist")
            return 1
        else:
            #print("No such a buddy")
            return None
        #print(myresult)
        mycursor.close()
        #mydb.close()

    def sendFriendReq(self,to_usrname):
        find=self.searchBuddy(to_usrname)             
        
        if(find==1):
            #First find id of requested buddy
            val=(to_usrname)
            mycursor = mydb.cursor()
            mycursor.execute("select userID from _user where usrname= %s ",(val,))
            myresult = mycursor.fetchall()
            #print(myresult)
            to_userID=int(myresult[0][0])
            #print(to_userID)
            mycursor.close()
    
            #check if friend request is already sent
            req=(self.userID,to_userID)
            check_cursor=mydb.cursor()
            check_cursor.execute("select * from buddy_req where from_user= %s and to_user= %s",req)
            exist=check_cursor.fetchall()
            if(len(exist)!=0):
                print("Friend request already sent")
                check_cursor.close()
            else:
                check_cursor.close()
                val_2=(self.userID,to_userID)
                mycursor2 = mydb.cursor()
                mycursor2.execute("insert into buddy_req (from_user,to_user) values (%s ,%s)",val_2)
                mydb.commit()
                print(mycursor2.rowcount, "friend request sent")
                mycursor2.close()
                mydb.close()
        else:
            print("User:"+str(to_usrname)+" doesn't exist or mispelled\nPlease try again")
        #print("from user: "+str(self.userID))
        #print("to user: "+str(to_user.userID))

        
    def showFriendReq(self):
            friend_req=[]
            val=(self.userID)
            mycursor = mydb.cursor()
            mycursor.execute("select _user.usrname,userID from _user,(select from_user from buddy_req where to_user=%s) as w where userID=w.from_user ",(val,))
            myresult = mycursor.fetchall()
            for coloumn in myresult:
                for values in coloumn:
                    friend_req.append(values)
                    #print(values)
            print(friend_req)
            return friend_req
            mycursor.close()

    def acceptFriendReq(self,from_usrname):
        #Find from_id from from_username
        val=(from_usrname)
        mycursor = mydb.cursor()
        mycursor.execute("select userID from _user where usrname= %s",(val,))
        myresult = mycursor.fetchall()
        #print(myresult)
        from_userID=int(myresult[0][0])
        #print(to_userID)
        mycursor.close()

        val_=(from_userID,str(self.userID))
        mycursor_1 = mydb.cursor()
        mycursor_1.execute("update buddy_req set is_accepted=1 where from_user= %s and to_user= %s ",val_)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        mycursor_1.close()

    def denyFriendReq(self,from_usrname):
            #Find from_id from from_username
            val=(from_usrname)
            mycursor = mydb.cursor()
            mycursor.execute("select userID from _user where usrname= %s ",(val,))
            myresult = mycursor.fetchall()
            #print(myresult)
            from_userID=int(myresult[0][0])
            #print(to_userID)
            mycursor.close()

            val_=(from_userID,str(self.userID))
            mycursor_1 = mydb.cursor()
            mycursor_1.execute("update buddy_req set is_accepted=2 where from_user= %s and to_user= %s",val_)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
            mycursor_1.close()



        
    
mydb= mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="pasatempo64",
        database="whatnau")

'''user1=User(4)#Bobos
user2=User(3)#jason
#user2.sendFriendReq("Bobos")
user1.denyFriendReq("Marinero")'''
mydb.close()


