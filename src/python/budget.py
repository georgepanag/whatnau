import mysql.connector


mydb= mysql.connector.connect(
host="localhost",
user="root",
passwd="pasatempo64",
database="whatnau")

class Budget:

    def __init__(self):
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
        
        
        if (myresult) != None:
            print("The connection with the credit card was successful!")
            print("The credit card's number is :")
            print(myresult)
            return 1
        else:
            print("The credit card can not be found")
            return None
        

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

    def get_money_spent (self,userID,money_spent ):
        val2=userID
        val=money_spent
        total_spent_money=val
        total_spent_money= total_spent_money+ val
        
        
        mycursor = mydb.cursor()
        
        sql="update _budget set monthly_budget = %s where userID=%s"
        variable=(total_spent_money, userID)
        mycursor.execute(sql, variable)
        #myresult2 = mycursor.fetchone()
        
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        
        mycursor.execute=("select budget_upper_bound from _budget where userID=%s ",(val2,))
        myresult = mycursor.fetchone()
        print(myresult) #Prints result as tuple
        mycursor.close()
        #mydb.close()
        

        
#create an object "budget1" for testing the functions by adding arguments to them
budget1=Budget
#budget1.select_day()
#budget1.credit_card_connection()
#budget1.set_budget_upper_bound()
#budget1.get_money_spent()
