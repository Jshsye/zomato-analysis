# total no. of orders
import pandas as pd

df= pd.read_csv("zomato.csv", encoding='latin1')
pd.set_option("display.max_column", None)
total_orders= df["url"].count()
print(total_orders)

# its first step where i need to check where how many records it contain from this i got that i analyzed with approx 51717 records in the data and it means  50+ records are contain in dataset