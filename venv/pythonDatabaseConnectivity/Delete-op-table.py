from utilityForDatabase import Utility

mydb=Utility.dataBase()
mycursor=mydb.cursor()

sql="delete from employee where name='sandy'"

mycursor.execute(sql)
mydb.commit()