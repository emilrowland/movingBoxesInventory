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
        res = {'ID': cursor.lastrowid, 'content': content, 'status': status}
        return res

    def print_list_of_moving_boxes(self):
        moving_boxes = self.conn.execute('SELECT * FROM movingBoxes')
        for i in moving_boxes:
            print(i)
