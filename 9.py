# top 5 rest_type

import pandas as pd

df= pd.read_csv("zomato.csv", encoding='latin1')
pd.set_option("display.max_column", None)
# print(df.head(2))

group_rest_type= df.groupby("rest_type")["rest_type"].count().head(5)
print(group_rest_type)


# here i am trying to analyze for which type of resturant are highest sales or customer because it help me to increase the inventory of there and maintain upto date
