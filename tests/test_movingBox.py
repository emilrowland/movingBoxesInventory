import unittest
import os
from pathlib import Path
from movingBoxesInventory import movingBox


class TestMovingBox(unittest.TestCase):
    def setUp(self):
        self.db = movingBox.MovingBox()
        self.path_to_db = 'movingBoxes.db'

    def tearDown(self):
        del self.db
        os.remove(self.path_to_db)

    def test_create_database(self):
        self.assertTrue(Path(self.path_to_db))

    def test_add_moving_box(self):
        box_id = self.db.add_moving_box('content1', 'place1')
        self.assertTrue(self.db.get_moving_box(box_id))
        self.db.add_moving_box('content2', 'place2')
        self.assertEqual(len(self.db.get_all_moving_boxes()), 2)
