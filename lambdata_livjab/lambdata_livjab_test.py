import unittest
from null_handling import ReplaceNulls
import pandas as pd
import numpy as np

class null_test(unittest.TestCase):

    def test_nulls(self):
        d = {"col": [6, 7, np.nan, 9],
             "col2": [34, np.nan, 68, 48],
             "col3": [30, 20, 20, np.nan]}
        null_df = pd.DataFrame(data=d).astype(float)
        self.assertEqual(ReplaceNulls.null_handler(self, null_df).isnull().sum().sum(), 0)

if __name__ == '__main__':
    unittest.main()
