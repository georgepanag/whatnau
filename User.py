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
        #Find -from_id- from -from_username-
        val=(from_usrname)
        mycursor = mydb.cursor()
        mycursor.execute("select userID from _user where usrname= %s",(val,))
        myresult = mycursor.fetchall()
        #print(myresult)
        from_userID=int(myresult[0][0])
        #print(to_userID)
        mycursor.close()

        #update table buddy_req
        val_=(from_userID,str(self.userID))
        mycursor_1 = mydb.cursor()
        mycursor_1.execute("update buddy_req set is_accepted=1 where from_user= %s and to_user= %s ",val_)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        mycursor_1.close()

        #update table buddies
        val_2 =(self.userID,from_userID)
        mycursor_2 = mydb.cursor()
        mycursor_2.execute("insert into buddies (userID,buddy) values (%s, %s)",val_2)
        mydb.commit()
        print(mycursor.rowcount, "A new friendship begins...")
        mycursor_2.close()
        

        

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


    def getBuddiesID(self):
        buddies_list=[]
        val=(self.userID)
        mycursor = mydb.cursor()
        mycursor.execute("select buddy from buddies where buddies.userID= %s ",(val,))
        myresult = mycursor.fetchall()
        #print(myresult)
        for pair in myresult:
            for buddyID in pair:
                buddies_list.append(buddyID)
        #print(buddies_list)
        return buddies_list
        mycursor.close()
        
    def showFriendsEvents(self):
        b=self.getBuddiesID()
        print(b)
        #v=("YES")
        shared={}
        tuples_usrnms=[]
        tuples_events=[]
        for ids in b:
            mycursor_usrnames = mydb.cursor()
            mycursor_usrnames.execute("select usrname from _user,_event where  _event.userID=_user.userID and _event.shared='YES' and _user.userID="+str(ids))
            myresult_usrnames = mycursor_usrnames.fetchall()    
            #print(myresult_usrnames)
            tuples_usrnms.append(myresult_usrnames)
            
            
            mycursor_events=mydb.cursor()
            mycursor_events.execute("select descr, start_date, _end_date from _event where shared='YES' and start_date <= now() and userID="+str(ids))
            myresult_events = mycursor_events.fetchall()
            #print(myresult_events)
            tuples_events.append(myresult_events)
        
        
        
        #print(tuples_usrnms)
        #print(tuples_events)
        f_usrnms=[]
        f_events=[]
        
        for pair in tuples_usrnms:
            for usrname in pair:
                f_usrnms.append(usrname)
        #print(f_usrnms)

        for pair in tuples_events:
            for event in pair:
                f_events.append(event)
        #print(f_events)

        for i in range(len(f_events)):
            #print(f_events[i][2])
            return str(f_usrnms[i][0])#User's username
            return str(f_events[i][0])#event's description
            return f_events[i][1].year#event's starting date
            return f_events[i][1].month
            return f_events[i][1].day
            return f_events[i][1].hour
            return f_events[i][1].minute
            return f_events[i][2].year#event's expired date
            return f_events[i][2].month
            return f_events[i][2].day
            return f_events[i][2].hour
            return f_events[i][2].minute
            
        
    
'''for testing
mydb= mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="whatnau")

user1=User(1)#Bobos
user2=User(3)
#user2.sendFriendReq("Bobos")
user1.showFriendsEvents()
mydb.close()
'''

