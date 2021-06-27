import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "your_password_here"
)


mycursor = db.cursor()   # creating cursor object

mycursor.execute("CREATE DATABASE student")   # creating a schema for student database
