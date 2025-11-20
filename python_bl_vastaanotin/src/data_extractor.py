import mysql.connector
import csv
import os

mydb = mysql.connector.connect(
  host=os.getenv("DATABASE_IP"),
  password=os.getenv("DATABASE_PASSWORD"),
  user="dbaccess_rw",
  database="measurements"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT sensorvalue_a, sensorvalue_b, sensorvalue_c FROM rawdata WHERE groupid = 9")

myresult = mycursor.fetchall()

with open("data_from_db.csv", "w") as csvfile:
    writer = csv.writer(csvfile, lineterminator="\n")  
    writer.writerow(["x", "y", "z"])
    for a, b, c in myresult:
        writer.writerow([a, b, c])
      