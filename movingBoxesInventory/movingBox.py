import sqlite3


class MovingBox:
    def __init__(self):
        self.conn = sqlite3.connect('movingBoxes.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS movingBoxes(
        ID integer primary key, content text, status text, createdDate text)''')

    def __del__(self):
        self.conn.close()
