def null_handler(df):
    for column in df:
        column.fillna(column.mean(), inplace=True)
