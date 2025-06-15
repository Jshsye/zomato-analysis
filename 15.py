import pandas as pd

df= pd.read_csv("zomato.csv")
pd.set_option("display.max_column", None)

dish_liked= df['dish_liked'].count()

# percent= (dish_liked/51717) * 100
print(dish_liked)

print(f"the percentage of dish liked:",(dish_liked / 51717)* 100,"%")

# i got that almost 45% of people liked the dishes we provide

# here i got that 45% peoples like the dishes we provide but i am not sure about this data as per the record i got that almost 45% of peoples are like with this...!