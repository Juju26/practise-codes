from logging import exception
import mysql.connector as mc

mydb=mc.connect(host="localhost",user="bot1",passwd="12345")
mycursor=mydb.cursor()
mycursor.execute("use dbfpython")

mycursor.execute("insert into usingpython values('Raj',1),('Raju',2),('Rajesh',3)")
mycursor.execute("insert into usingpython values('Rajaji',5),('Rajeshwari',6)")

mydb.commit()  # commit the changes to the database
mycursor.execute("select * from usingpython")
print(mycursor.fetchall())
