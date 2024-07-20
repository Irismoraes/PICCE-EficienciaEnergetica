import MySQLdb
db = MySQLdb.connect(
    host="localhost",
    user="admin",
    passwd="p#i2cc3",
    db="db_site"
)

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("MySQL version:", data)

db.close()

