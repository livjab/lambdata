# function that splits a date column into individual pieces and creates new columns for each
# this applies to dates in string format month-day-year -- Ex. "May 28 2019"

def date_split(df):
  import datetime

  # function to apply to date column
  def to_datetime(x):
    return datetime.datetime.strptime(x, "%b %d %Y")

  # create new column using function
  df["datetime"] = df["date"].apply(to_datetime)

  # change datetime column to string
  df["datetime"] = df["datetime"].astype(str)

  # separating date into year/month/day
  df["date_sep"] = df["datetime"].str.split("-")

  # create new features for each
  df["year"] = pd.to_numeric(df["date_sep"].str[0])
  df["month"] = pd.to_numeric(df["date_sep"].str[1])
  df["day_of_month"] = pd.to_numeric(df["date_sep"].str[2])

  # drop sep column
  df = df.drop(columns="date_sep")

  return df


"""
Example data
"""
#import numpy as np
#import pandas as pd

#d = {"col": [6, 7, 8], "date": ["May 28 2019", "Jun 03 2019", "Jul 12 2014"]}

#df = pd.DataFrame(data=d)

#df["date"] = df["date"].astype(str)

#date_split(df)
