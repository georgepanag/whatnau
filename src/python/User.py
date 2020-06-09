import mysql.connector
import datetime
from Event import Event
from datetime import datetime
<<<<<<< HEAD

=======
>>>>>>> yiorgos

class User():

    def __init__(self,userID):
        self.userID=userID
        self.events=[]
        
        '''
        self.email=space
        self.usrname=usrname
        self.interest=interest
        self.gender=interest
        self._type=_type
        self.job=job
        self.corporation=corporation
        self.space=space'''
        

    def getEventsFromDB(self, mydb):
        events=[]
        mycursor = mydb.cursor()
        mycursor.execute("select _event.* from _event,_user where _user.userID =_event.userID and _user.userID= %s ",(self.userID,))
        myresult = mycursor.fetchall()
        for evnt in myresult:
            self.events.append(Event(evnt[0],evnt[1],evnt[2],evnt[3],evnt[4],evnt[5],evnt[6]))
        mycursor.close()
    
    def showListEvents(self,mydb):#show user's events
        events=[]
        val=(self.userID)
        mycursor = mydb.cursor()
        mycursor.execute("select _event.* from _event,_user where _user.userID =_event.userID and _user.userID= %s ",(val,))
        myresult = mycursor.fetchall()
        '''for coloumn in myresult:
            for values in coloumn:
                events.append(values)
                #print(values)
        print(events)
        return events'''
        print(myresult)
        return(myresult)
        mycursor.close()
        #mydb.close()

    def overlappingEvents(self,start_,end_):#checkConflicts
        s=datetime.strptime(str(start_),'%Y-%m-%d %H:%M:%S')#convert into datetime for better manipulation
        e=datetime.strptime(str(end_),'%Y-%m-%d %H:%M:%S')
        datetimes=[]
        x=self.showListEvents(mydb)
        #get datetime instanses
        for i in x:
            #if isinstance(i,datetime):
            datetimes.append(i[5])
            datetimes.append(i[6])
<<<<<<< HEAD
        print(datetimes)
        print("hjhhkklhjhj")
=======
>>>>>>> yiorgos
        
        #check for overlapping events
        
        d=0
        overlap=0
        #r1 = Range(start=start_, end=end_)
        while(d!=len(datetimes)):
            #r2 = Range(start=datetimes[d], end=datetimes[d+1])
            print("start="+str(datetimes[d])+"\nend="+str(datetimes[d+1]))
            if not(((s < datetimes[d]) and (e < datetimes[d])) or ((s >datetimes[d+1]) and (e >datetimes[d+1]))):
                overlap+=1
            else:
                overlap+=0
            '''latest_start = max(r1.start, r2.start)
            earliest_end = min(r1.end, r2.end)
            delta = (earliest_end - latest_start).days + 1
            overlap = max(0, delta)
            print(overlap)'''
            
            d+=2
        if(overlap!=0):
<<<<<<< HEAD
            print("OVERLAP OCCURS")
            print(overlap)
=======
>>>>>>> yiorgos
            return 1
        else:
            print("NO overlap")
            print(overlap)
            return 0
       



        
    def showUrgEvents(self,mydb):
        urg_events=[]
        val=(self.userID)
        mycursor = mydb.cursor()
        mycursor.execute("select _event.* from _event,_user where _user.userID =_event.userID and _event.importance='HIGH' and _user.userID= %s ",(val,))
        myresult = mycursor.fetchall()
        for coloumn in myresult:
            for values in coloumn:
                urg_events.append(values)
                #print(values)
        print(urg_events)
        return urg_events
        mycursor.close()
        #mydb.close()

    #checks shared space availability for user with self.userID
    def sharedSpaceFull(self,mydb):
        val=(self.userID)
        mycursor = mydb.cursor()
        mycursor.execute("select shared_space from _user where userID= %s ",(val,))
        myresult = mycursor.fetchall()
        shared=myresult[0][0]
        print(shared)
        mycursor.close()
        if(shared==5):#full space
            return 1
        if(shared==0):#avoids shared_space from getting negative values
            return 2
        else: #not full space
            return 0
        
     def get_promoted_events(self,category,mydb):
        val =(category)
        
        mycursor = mydb.cursor()
        
        mycursor.execute("select * from promoted_event where target_aud= 'only fans' and category LIKE %s",(val,))
        
        
        myresult = mycursor.fetchall()
        #print (myresult)
        return (myresult)
        mycursor.close()    
        
       
        
    def addEvent(self,descr,_type,importance,start_date,_end_date,shared,mydb): #To userID to pairnei automata apo to User antikeimeno
        
        if(shared=="YES"):
            if(self.sharedSpaceFull(mydb)==1):
                print("full shared space")
            if(self.sharedSpaceFull(mydb)==2):
                print("<im in elif> ")
                
                print("Shared event space is full.\nPLEASE REMOVE SOME SHARED EVENTS OR MODIFY THE CORRESPONDING LABEL<shared>\n")
                
            else:
                print("<im in else> ")
                
                #(First)Check for event conflicts
                conflict=self.overlappingEvents(start_date,_end_date)
                if(conflict!=1):
                    val1=(self.userID,descr,_type,importance,start_date,_end_date,shared)
                    mycursor = mydb.cursor()
                    mycursor.execute("insert into _event(userID,descr,_type,importance,start_date,_end_date,shared) values (%s, %s, %s, %s, %s, %s, %s)",val1)               
                    print(mycursor.rowcount, "event created")
                    mycursor.close()
                   #updates shared_space every time a user shares an event
                    val2=(self.userID)
                    mycursor_1 = mydb.cursor()
                    mycursor_1.execute("update _user set shared_space=shared_space - 1 where userID = %s ",(val2,))
                    mydb.commit()
                    print(mycursor.rowcount, "record(s) affected")
                    mycursor_1.close()

                else:
                    print("conflict occcur")
        if shared=="NO":
            #(First)Check for event conflicts
            conflict=self.overlappingEvents(start_date,_end_date)
            if(conflict!=1):
                val3=(self.userID,descr,_type,importance,start_date,_end_date,shared)
                mycursor = mydb.cursor()
                mycursor.execute("insert into _event(userID,descr,_type,importance,start_date,_end_date,shared) values (%s, %s, %s, %s, %s, %s, %s)",val3)
                mydb.commit()               
                print(mycursor.rowcount, "event created")
                mycursor.close()
            else:
                print("conflict occcur")    

        
        

    def searchBuddy(self,buddy_usrname,mydb):
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

    def sendFriendReq(self,to_usrname,mydb):
        find=self.searchBuddy(to_usrname,mydb)             
        
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

        
    def showFriendReq(self,mydb):
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

    def acceptFriendReq(self,from_usrname,mydb):
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
        

        

    def denyFriendReq(self,from_usrname,mydb):
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


    def getBuddiesID(self,mydb):
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
        
    def showFriendsEvents(self,mydb):
        b=self.getBuddiesID(mydb)
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
<<<<<<< HEAD
=======
            
        
>>>>>>> yiorgos

    def confirmAsParticipant(self,promotedID,mydb):
        val =(self.userID,promotedID)
        mycursor = mydb.cursor()
        mycursor.execute("insert into participants(userID,promotedID) values (%s, %s)",val)
        mydb.commit()
        print(mycursor.rowcount, "Add to participants...")
        mycursor.close()

    def AddCritique(self,promotedID,critique,mydb):
        val=(critique,self.userID,promotedID)
        mycursor = mydb.cursor()
        mycursor.execute("update participants set review_score= %s  where userID= %s and promotedID= %s",val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        mycursor.close()
