# how many online ordered
import pandas as pd

df= pd.read_csv("zomato.csv", encoding='latin1')
pd.set_option("display.max_column", None)

print(df["online_order"].isnull().sum())

online_order= df.groupby('online_order')['online_order'].value_counts()
print(online_order)

percent= (online_order / 51717) * 100

print(df['online_order'].count(), percent)

# online orders are 30444 which means 58.86% percentage of orders are online orders
# not online orders are 21273 and 41.13 % of orders are not online orders

# from this analysis we got that online order is more than offline orders. where our online customers are almost 58% so we need to check whether our delivery of items are in correct time or delay in delivery so that we can grow online order more than the current ratio
