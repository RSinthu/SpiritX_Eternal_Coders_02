import pymysql

# Connect to MySQL using pymysql
db_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",  # Provide your MySQL password here
    database="CricketGame",
    cursorclass=pymysql.cursors.DictCursor
)