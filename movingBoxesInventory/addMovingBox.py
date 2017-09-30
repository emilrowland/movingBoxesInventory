import utility
from getMovingBox import GetMovingBox

class AddMovingBox:
    def __init__(self, moving_box_db):
        self.db = moving_box_db

    def add_moving_box(self):
        utility.clear_console()
        print("Add new moving box")
        content = input("What does the moving box contain? ")
        status = input("Where is the moving box now? ")
        res = self.db.add_moving_box(content, status)
        print("Added new moving box with data")
        moving_box = GetMovingBox(self.db)
        utility.print_moving_box(moving_box.get_moving_box(res))
        print()

