from utilityForDatabase import Utility

mydb=Utility.dataBase()
mycursor=mydb.cursor()

mycursor.execute("show tables ")
for tb in mycursor:
    print(tb)


