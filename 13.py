# location wise sales

import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("zomato.csv", encoding='latin1')
pd.set_option("display.max_column", None)

df['approx_cost(for two people)'] = df['approx_cost(for two people)'].str.replace(',', '').astype(float)

location_wise = df.groupby('location')['approx_cost(for two people)'].sum().head(10)

plt.figure(figsize=(12,6))
plt.plot(location_wise.index, location_wise.values)
plt.xticks(rotation=90)
plt.xlabel("Location")
plt.ylabel("Total Cost for Two")
plt.title("Total Approx Cost for Two People by Location")
plt.tight_layout()
plt.savefig('location wise.png')
plt.show()

# i tried to know which are the top location of sales it will help me to know about sales and inventory and need to maintain stock there