import unittest
from src.db import get_engine, _inspect_db


class MyTestCase(unittest.TestCase):
    def test_connect_db(self):
        eng = get_engine()

    def test_inspect_db(self):
        assert _inspect_db()




if __name__ == '__main__':
    unittest.main()
