import mysql.connector


mydb= mysql.connector.connect(
host="localhost",
user="root",
passwd="password",
database="whatnau")

class Budget:
    
 
    def __init__(self,userID):
        self.userID=userID

    def select_day(self,choose_day, choose_user):
        val=choose_day
        
        # σύνδεση με το gui
        #val= input(" please choose a day: ")
        
        mycursor = mydb.cursor()
        sql="update _budget set day_selection= %s where userID=%s"
        variable=(val, choose_user)
        mycursor.execute(sql, variable)

        #mycursor.execute("update _budget set day_selection= '18' where userID=2")
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")

        mycursor.close()
        #mydb.close()



    def credit_card_connection(self,userID):
        val=userID
        mycursor = mydb.cursor()
        #mycursor.execute("select cr_cardID from _budget where _budget.userID=_user.userID and _user.userID=%s ",(val,))
        mycursor.execute("select cr_cardID from _user where userID=%s ",(val,))
        
        myresult = mycursor.fetchone()
        
        
        if (myresult) != None :
            print("The connection with the credit card was successful!")
            print("The credit card's number is :")
            print (str(myresult[0]))
            return str(myresult[0])
            
        else:
            print("The credit card can not be found")
            #return None
        

        mycursor.close()
        #mydb.close()

    def set_budget_upper_bound (self,userID,budget_upper_bound):
        val=budget_upper_bound
        mycursor = mydb.cursor()

        sql="update _budget set budget_upper_bound = %s where userID=%s"
        variable=(val, userID)
        mycursor.execute(sql, variable)

        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        

        mycursor.close()
       #mydb.close()
         
#In the next method, the money that the user spends had to be added automatically to the month by the credit card(if we had a real credit card).
#Here, the user adds the money he spent by his/her own.


    def add_money_spent (self,userID,money_spent ):
        val= userID
        mycursor1 = mydb.cursor()
        
        mycursor1.execute("select monthly_budget from _budget where userID=%s ",(val,))
        
        myresult = mycursor1.fetchone()
        already_spent= int( myresult[0])
        print(already_spent)
        
        
        mycursor1.close()

        val2=money_spent
        
        
        
        
        
        total_money_spent=already_spent+val2
        
        
        
        mycursor2 = mydb.cursor()
        
        sql="update _budget set monthly_budget = %s where userID=%s"
        variable=(total_money_spent, userID)
        mycursor2.execute(sql, variable)
       
        
        mydb.commit()
        print(mycursor2.rowcount, "record(s) affected")
        
        
        
        
        
        mycursor2.close()
        #mydb.close()

    def check_upper_bound( self,userID):
        val=userID
        val2=userID 
        
        mycursor = mydb.cursor()
        mycursor.execute("select budget_upper_bound from _budget where userID=%s ",(val,))
        
        myresult = mycursor.fetchone()
        #print (int(myresult[0])) #just checking the rusult
        mycursor.close()



        mycursor1 = mydb.cursor()
        mycursor1.execute("select monthly_budget from _budget where userID=%s ",(val2,))
        
        myresult2 = mycursor1.fetchone()
        #print (int(myresult2[0])) #just checking the result
        
        mycursor1.close()

        if myresult2>myresult:
            print("Upper_bound_exceeded!")

        
        
        

        
#create an object "budget1" for testing the functions by adding arguments to them
budget1=Budget(1)
#budget1.select_day(16,1)
#budget1.credit_card_connection(1)
#budget1.set_budget_upper_bound(1,100)
#budget1.add_money_spent(3,200)
#budget1.check_upper_bound(1)
