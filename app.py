import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="NaveedKhan123",
  database="ecommercepython"
)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM products")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

