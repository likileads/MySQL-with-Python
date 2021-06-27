import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "your_password_here",
    database = "student"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE basic_details( student_id int PRIMARY KEY AUTO_INCREMENT, sname VARCHAR(25), address VARCHAR(25), age smallint UNSIGNED)")

#--------understand-----------

'''
int --> for integer value
smallint --> used for age since age won't be a large int
unsigned --> age is unsigned to ensure it doesn't take a negative value
varchar --> used for alphanumeric values
primary key --> the key which is unique for each entry
auto_increment --> used with primary key to automatically generate a primary key which is greater or unique compared to the previous entry
...
