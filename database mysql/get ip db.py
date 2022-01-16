import mysql.connector as mc

name=input("Enter your name: ")
rollno=int(input("Enter your rollno: "))


mydb=mc.connect(host="localhost",user="bot1",passwd="12345")
mycursor=mydb.cursor()
mycursor.execute("use dbfpython")
mycursor.execute("create table if not exists usingpython(name varchar(20),rollno int(10))")
mycursor.execute("insert into user_input_db values('%s',%d)"%(name,rollno))
mydb.commit()
mycursor.execute("select * from user_input_db")