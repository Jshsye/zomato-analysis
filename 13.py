import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("zomato.csv", encoding='latin1')
pd.set_option("display.max_column", None)
# print(df.head(2))

df['approx_cost(for two people)'] = df['approx_cost(for two people)'].str.replace(',', '').astype(float)

listed_in_city_grouped= df.groupby("listed_in(city)")["approx_cost(for two people)"].sum().head(5)

print(listed_in_city_grouped)

plt.pie( listed_in_city_grouped.values, labels= listed_in_city_grouped.index, autopct='%1.1f%%' )
plt.title("City wise sales analysis")
plt.tight_layout()
plt.savefig('city sales.png')
plt.show()

# top 5 cities highest sales

# top 1 is BTM which is 41.2%, 2} bannerghat rd which is 18.6% , 3} ballendur which is almost 17.1% sales,  4} basavanagudi which is 14.3%, and last is banashankari 8.8%

# i want to know which are the top 5 cities that we have and what are the improvemnt did there so that all the cities can make more sales
