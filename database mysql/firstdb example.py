#pip3 install mysql-connector

import mysql.connector as mc

mydb=mc.connect(host="localhost",user="bot1",passwd="12345",database="dbfpython")
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM firsttable")
myresult=mycursor.fetchall()
print(myresult)