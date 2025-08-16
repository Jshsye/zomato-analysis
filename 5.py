# how namy of this had booked with table

import pandas as pd

df= pd.read_csv("zomato.csv", encoding='latin1')
pd.set_option("display.max_column", None)

table_booked= df.groupby('book_table')['book_table'].value_counts()
print(table_booked)
percnt= (table_booked / 51717) * 100
print(percnt)

# booked with table 6449 which means only 12.46% with table booked
# without table are 45268 which means almost 87.53%

# from this we got that we should not invest more in furnitures or like table chairs etc.. orr...  otherwise we need to reduce the chair and table for the customers as the customer will either take online delivery or parcel alomst above 80% so need to check about it in depth
