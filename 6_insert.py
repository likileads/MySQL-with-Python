import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "your_password_here",
    database = "student"
)

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE basic_details( student_id int PRIMARY KEY AUTO_INCREMENT, sname VARCHAR(25), address VARCHAR(25), age smallint UNSIGNED)")

mycursor.execute("INSERT INTO basic_details (sname, address, age) VALUES ('Liki', 'Bengaluru', 21)")

mycursor.execute("SELECT * FROM basic_details")

for x in mycursor:
    print(x)
    
    
    
    
#----------OUTPUT-----------

# (1, 'Liki', 'Bengaluru', 21)
