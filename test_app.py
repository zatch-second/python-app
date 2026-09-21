import unittest
from app import fetch_data

class TestApp(unittest.TestCase):
    def test_fetch(self):
        self.assertEqual(fetch_data(), 1)

if __name__ == '__main__':
    unittest.main()