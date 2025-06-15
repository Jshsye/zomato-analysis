# described the data
import pandas as pd

df= pd.read_csv("zomato.csv", encoding='latin1')
pd.set_option("display.max_column", None)

print(df.head(1))
print(df.describe())

# all the data are in alphabetic so only rating can able to count