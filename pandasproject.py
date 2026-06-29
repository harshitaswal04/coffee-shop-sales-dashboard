import pandas as pd
df = pd.read_csv("salescoffee.csv")

df.fillna({'transaction_date':'01-01-2023', 'transaction_time':'07:6:11' , 'transaction_qty':1 ,'store_id': 6,'store_location': 'kotdwar','product_id':55,'unit_price':4,'product_category':'kuchbhilele','product_type':'kabab','product_detail':'spicy_kabab_with_momo_chatni'}, inplace=True)
df.dropna(subset=["transaction_id"])

df.to_csv('output.csv', index = False)















