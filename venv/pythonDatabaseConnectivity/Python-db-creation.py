import mysql.connector
import os
mydb = mysql.connector.connect(
    host="localhost",
    user=os.environ['user_name'],
    passwd=os.environ['password'])

print(mydb)
if(mydb):
    print("connection succesful")
else:
    print("connection unsuccesful")