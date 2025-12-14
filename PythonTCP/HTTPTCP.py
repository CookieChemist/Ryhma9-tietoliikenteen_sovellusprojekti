import requests
import csv

url="http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=9"

response=requests.get(url)
rows = response.text.strip().split("\n")
parsed = [row.split(";") for row in rows]

selected = [(cols[5], cols[6], cols[7]) for cols in parsed]

with open("testcsv.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(selected)

