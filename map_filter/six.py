product_prices=[1000,500,800,400,20000]

#display all product prices below 1000
new_price=[]

for(price in product_prices):
    if price<1000:
        new_price.append(price)

print(new_price)

