
from utilityForDatabase import Utility

mydb=Utility.dataBase()
mycursor=mydb.cursor()

sqlform="insert into employee(name,sal) values(%s,%s)"

employees = [("sandy",40000),("prady",45000),("virat",50000)]
mycursor.executemany(sqlform,employees)
mydb.commit()




