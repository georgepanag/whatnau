import mysql.connector



mydb=mysql.connector.connect(host="localhost",user="root",password="pasatempo64",database="whatnau") 
# Python program to create a table
   
from tkinter import *
  
  
class PostedEventsTable:
      
    def __init__(self,root,userID):

        mycursor = mydb.cursor()
        mycursor.execute("select * from _event where userID=+str(userID)")
        myresult = mycursor.fetchall()
        
        
        rows = len(myresult)
        
        columns =len(myresult[0])
          
        # code for creating table
        for i in range(rows):
            for j in range(columns):
                  
                self.e = Entry(root, width=12, fg='blue',
                               font=('Arial',16,'bold'))
                  
                self.e.grid(row=i, column=j)
                #print(sql_res[i][j])
                self.e.insert(END,str(myresult[i][j]))
  

        
root = Tk()
root.title("My Posted Events")
t = PostedEventsTable(root,userID)
root.mainloop()







mydb.close()
