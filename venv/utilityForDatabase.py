import mysql.connector
import os
class Utility:
    def dataBase():
        """
        :return: mydb
        """
        mydb = mysql.connector.connect(
            host="localhost",
            user=os.environ['user_name'],
            passwd=os.environ['password'],
            database="sandeep")
        return mydb
