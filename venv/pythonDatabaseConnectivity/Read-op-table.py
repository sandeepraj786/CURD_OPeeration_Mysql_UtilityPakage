from utilityForDatabase import Utility

mydb=Utility.dataBase()
mycursor=mydb.cursor()

mycursor.execute("select name from employee")

myresult=mycursor.fetchone()

for row in myresult:
    print(row)