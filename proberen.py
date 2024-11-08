import mysql.connector

print("let's go!")

woord = "maandag"
print(woord)

def eum(rset):
    print("rset: ", rset)

mydb = mysql.connector.connect(
  host="localhost",  #port erbij indien mac
  user="root",
  password="",
  database="autooverzicht"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM autos")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

for x in myresult:
    print("Merk: " + x[1] + " Nummerplaat: " + x[2])
    eum(x)

mijninvoer = input("Wat is je voornaam: ")
print(mijninvoer)


gaan = input("vul naam in")
sql = "INSERT INTO autos (merk, kenteken) VALUES (%s, %s)"
val = (gaan, 21)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")