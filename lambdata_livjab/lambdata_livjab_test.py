import unittest
from null_handling import ReplaceNulls


class null_test(unittest.TestCase):

    def test_nulls(self):
        self.assertEqual(df.isnull().sum(), 0)

if __name__ == '__main__':
    unittest.main()
