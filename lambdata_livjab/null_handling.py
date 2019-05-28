# fills all nulls with the mean value of its column

def null_handler(df):
    df = df.fillna(df.mean())
    return df

"""
Example code
"""

#d = {"col": [6, 7, np.nan, 9], "col2": [34, np.nan, 68, 48], "col3": [30, 20, 20, np.nan]}

#df = pd.DataFrame(data=d).astype(float)

# null_handler(df)
