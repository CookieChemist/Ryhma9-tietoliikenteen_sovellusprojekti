
import mysql.connector
import os

file = open("ble_notifications.txt", mode = "r", encoding = "utf-16")
lines = file.readlines()
file.close()

mydb = mysql.connector.connect(
  host=os.getenv("DATABASE_IP"),
  password=os.getenv("DATABASE_PASSWORD"),
  user="dbaccess_rw",
  database="measurements"
)

mycursor = mydb.cursor()
sql = "INSERT INTO rawdata (groupid, from_mac, to_mac, sensorvalue_a, sensorvalue_b, sensorvalue_c) VALUES (%s, %s, %s, %s, %s, %s)"

x = 0
for line in lines:
    if line == "0\n":
        sensorX = int(lines[x + 1])
        sensorY = int(lines[x + 2])
        sensorZ = int(lines[x + 3])
        val = (9, "D2:3F:48:D1:2D:F5", "B8:27:EB:25:BD:6C", sensorX, sensorY, sensorZ)
        mycursor.execute(sql, val)
        mydb.commit()
        print(f"x: {sensorX}\ny: {sensorY}\nz: {sensorZ}\n")
    x += 1

