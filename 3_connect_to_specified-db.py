import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "your_password_here",
    database = "student"    # edit
)

mycursor = db.cursor()

mycursor.execute("your_query_goes_here")
