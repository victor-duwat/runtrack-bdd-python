import mysql.connector

host = "localhost"
user = "root"
password = ""
database = "Laplateforme"


conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()

query = "SELECT nom, capacite FROM salle"
cursor.execute(query)

salles = cursor.fetchall()

for salle in salles:
    print(salle)

cursor.close()
conn.close()