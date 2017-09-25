import utility


class AddMovingBox():
    def __init__(self, movingBoxDB):
        self.db = movingBoxDB

    def add_moving_box(self):
        utility.clear_console()
        print("Add new moving box")
        content = input("What does the moving box contain? ")
        status = input("Where is the moving box now? ")
        res = self.db.add_moving_box(content, status)
        print("Added new moving box with data")
        print("ID: {0}".format(res['ID']))
        print("Content: {0}".format(res['content']))
        print("Status: {0}".format(res['status']))

