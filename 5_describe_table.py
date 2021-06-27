import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "your_password_here",
    database = "student"
)

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE basic_details( student_id int PRIMARY KEY AUTO_INCREMENT, sname VARCHAR(25), address VARCHAR(25), age smallint UNSIGNED)")

mycursor.execute("DESCRIBE basic_details")

for x in mycursor:
    print(x)
    
    
# --------------OUTPUT-------------------
'''
('student_id', b'int', 'NO', 'PRI', None, 'auto_increment')
('sname', b'varchar(25)', 'YES', '', None, '')
('address', b'varchar(25)', 'YES', '', None, '')
('age', b'smallint unsigned', 'YES', '', None, '')

'''
