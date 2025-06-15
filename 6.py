# how many are above rating of 4

import pandas as pd

df= pd.read_csv("zomato.csv", encoding='latin1')
pd.set_option("display.max_column", None)

df["rate_clean"]= df['rate'].astype(str).str.split('/').str[0].str.strip()

df['rate_clean']= pd.to_numeric(df['rate_clean'], errors='coerce')

rate_above_4= (df['rate_clean'] >= 4.0).value_counts()
pert= (rate_above_4 / 51717)* 100

print(rate_above_4)

print(f"\nIn percentage is : {pert}")


# here almost 23% of the sales is above 4 rating 
# above 4 rating is 12399

# from this code i got the rating here and i also faced some issue here that the data is not fully filtered in some of the column so i firstly cleaned the data and then i checked it i got result only 23 % of peoples are rating above 4 so there must be any reason for it