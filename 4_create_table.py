import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "dbms",
    database = "student"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE basic_details( student_id int PRIMARY KEY AUTO_INCREMENT, sname VARCHAR(25), address VARCHAR(25), age smallint UNSIGNED)")

