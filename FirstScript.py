import pymysql

pymysql.install_as_MySQLdb()
db = pymysql.connect(
    host="localhost",
    user="admin",
    passwd="54321",
    db="first_db1",
    charset="utf8"
)
cursor = db.cursor()
cursor.execute("""INSERT INTO Books(name, description)VALUES(%s, %s),(%s,%s)""",
               ("One", "Two",
                "Three", "Four")
               )
db.commit()
# cursor.execute("DELETE FROM Books WHERE id>1")
# db.commit()
cursor.execute("SELECT * FROM Books;")
books = cursor.fetchall()
for book in books:
    print(book)
cursor.close()
db.close()
