import mysql.connector

mydb = mysql.connector.connect(
  host="172.20.241.9",
  database="measurements",
  user="dbaccess_ro",
  password="vsdjkvwselkvwe234wv234vsdfas"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM rawdata WHERE groupid=82 ORDER BY id DESC LIMIT 600")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

with open('C:/Koulu (Tietotekniikka)/anturidataa/dataa2.csv', 'w') as f:
  f.write(myresult)