from utilityPackage import Utility

mydb=Utility.dataBase()
mycursor=mydb.cursor()

mycursor.execute("show databases")

for db in mycursor:
    print(db)






