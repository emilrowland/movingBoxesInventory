import unittest
import os
from pathlib import Path
from movingBoxesInventory.movingBox import MovingBox


class TestMovingBox(unittest.TestCase):
    def setUp(self):
        self.db = MovingBox()
        self.path_to_db = 'movingBoxes.db'

    def tearDown(self):
        del self.db
        os.remove(self.path_to_db)

    def test_create_database(self):
        self.assertTrue(Path(self.path_to_db))
