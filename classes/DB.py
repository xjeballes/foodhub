import mysql.connector
from mysql.connector import errorcode
from classes.Singleton import Singleton

@Singleton
class DB():
    mydb = None
    def conn(self):
        if self.mydb is None:
            try:
                self.mydb = mysql.connector.connect(user='root',password='',host="127.0.0.1",database='foodhub')   
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("MySQL Error: Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("MySQL Error: Database does not exist")
                else:
                    print(err)
        return self.mydb
    
    def cursor(self):
        return self.mydb.cursor()
