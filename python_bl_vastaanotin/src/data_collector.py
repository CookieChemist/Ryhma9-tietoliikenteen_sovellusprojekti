import mysql.connector

mydb = mysql.connector.connect(
  host="172.20.241.9",
  user="dbaccess_rw",
  password="fasdjkf2389vw2c3k234vk2f3",
  database="measurements"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT sensorvalue_a, sensorvalue_b, sensorvalue_c FROM rawdata WHERE groupid = 9")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)