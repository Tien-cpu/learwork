import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="db_haircut")

mycursor = mydb.cursor()

mycursor.execute("select id,name from saloncategory")
for i in mycursor:
    print(i[1])
