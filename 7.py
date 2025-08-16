# remove "[]" from the menu column and adding nan or non in it
import pandas as pd

df= pd.read_csv("zomato.csv", encoding='latin1')
pd.set_option("display.max_column", None)

df["menu_item"] = df["menu_item"].astype(str).str.replace(r"[\[\]]", "", regex=True).replace("Nan", pd.NA)


# print(df.head(50))

print(df["menu_item"].isnull().sum())

# this had made the removing unwanted data to store so removed unwanted data from the table
