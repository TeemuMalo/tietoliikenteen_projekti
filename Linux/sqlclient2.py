import mysql.connector
import login as log

mydb = mysql.connector.connect(
  host=log.HOST_IP,
  database=log.DATABASENAME,
  user=log.USERNAME,
  password=log.PASSWORD
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM rawdata WHERE groupid=82 ORDER BY id DESC LIMIT 600")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

with open('C:/Koulu (Tietotekniikka)/anturidataa/dataa3.csv', 'w') as f:
  f.write(myresult)