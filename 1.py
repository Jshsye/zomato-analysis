import pandas as pd

df= pd.read_csv("zomato.csv")
pd.set_option("display.max_column", None)
print(df.head())
