def date_split(df["date"]):
  # separating date into year/month/day columns
  df["date_sep"] = df["date"].str.split("-")

  # create new features for each
  df["year"] = pd.to_numeric(df["date_sep"].str[0])
  df["month"] = pd.to_numeric(df["date_sep"].str[1])
  df["day_of_month"] = pd.to_numeric(df["date_sep"].str[2])

  # drop separated column
  df = df.drop(columns="date_sep")
