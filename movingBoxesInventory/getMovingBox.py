import utility


class GetMovingBox():
    def __init__(self, moving_box_db):
        self.db = moving_box_db

    def get_moving_box(self, box_id):
        moving_box = self.db.get_moving_box(box_id)
        return moving_box

    def interface(self):
        utility.clear_console()
        print("Get information on moving box")
        try:
            box_id = int(input("Moving box ID: "))
            box = self.get_moving_box(box_id)
            if box:
                utility.print_moving_box(box)
            else:
                print("There is no moving box with ID: {0}".format(box_id))
        except ValueError:
            print("ID needs to be an integer!")
        print()