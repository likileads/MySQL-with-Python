# basic structure to connect to MySQL database

import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "your_password_here"
)


mycursor = db.cursor()   # creating cursor object

mycursor.execute("your_query_goes_here")
