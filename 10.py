# graphical represented the rest type

import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("zomato.csv", encoding='latin1')
pd.set_option("display.max_column", None)
print(df.head(2))

group_rest_type= df.groupby("rest_type")["rest_type"].count().head(5)

plt.figure(figsize=(10,6))
plt.bar(group_rest_type.index, group_rest_type.values, color='red')
plt.xlabel('Restaurant Type')
plt.ylabel('Count')
plt.title('Top 5 Restaurant Types in Zomato Dataset')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Top 5 Resturant.png")
plt.show()

# from this i checked the graphical representation for clear picture of sales in resturant type
