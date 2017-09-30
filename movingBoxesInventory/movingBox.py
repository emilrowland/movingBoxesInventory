import sqlite3


class MovingBox:
    """Handle the moving box database"""
    def __init__(self):
        self.conn = sqlite3.connect('movingBoxes.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS movingBoxes(
        ID integer primary key, content text, status text, createdDate text)''')

    def __del__(self):
        self.conn.close()

    def add_moving_box(self, content, status):
        cursor = self.conn.cursor()
        cursor.execute("""INSERT INTO movingBoxes (content, status, createdDate)
        VALUES ('{0}','{1}', DATETIME('now','localtime'))""".format(content, status))
        self.conn.commit()
        res = cursor.lastrowid
        return res

    def get_moving_box(self, box_id):
        moving_box = self.conn.execute("SELECT * FROM movingBoxes WHERE ID = {0}".format(box_id))
        return moving_box.fetchone()

    def get_all_moving_boxes(self):
        moving_boxes = self.conn.execute('SELECT * FROM movingBoxes')
        return moving_boxes
