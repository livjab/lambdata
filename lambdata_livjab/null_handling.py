"""
 Fills all nulls in a dataframe with the mean value of its column
 """

class ReplaceNulls:

    def __init__(self, df=None):
        self.df = df

    def null_handler(self, df):
        df = df.fillna(df.mean())
        return df

"""
Example code

d = {"col": [6, 7, np.nan, 9],
     "col2": [34, np.nan, 68, 48],
     "col3": [30, 20, 20, np.nan]}

null_df = pd.DataFrame(data=d).astype(float)

replace_nulls = ReplaceNulls()
repalce_nulls.null_handler(null_df)
"""
