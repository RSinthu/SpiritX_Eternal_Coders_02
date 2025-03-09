from db.db import db_connection

cursor = db_connection.cursor()  

def get_all_players():
    cursor.execute("SELECT * FROM cricketers")
    rows = cursor.fetchall()
    return [dict(row) for row in rows]