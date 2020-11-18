from utilityForDatabase import Utility

mydb=Utility.dataBase()
mycursor=mydb.cursor()

sql="update employee set sal=70000 where name='sandy'"
mycursor.execute(sql)

mydb.commit()