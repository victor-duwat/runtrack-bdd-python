import mysql.connector


host = "localhost"
user = "root"
password = ""
database = "LaPlateforme"

# Connexion
conn = mysql.connector.connect(host = host, user = user, password = password, database = database)
cursor = conn.cursor()

query = "SELECT * FROM etudiant"
cursor.execute(query)

#resulta
students = cursor.fetchall()

for student in students:
    print(student)


cursor.close()
conn.close()