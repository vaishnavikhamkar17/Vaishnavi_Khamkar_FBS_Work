## WAP to calculate profit or loss.

cost_price = int(input('Enter the cost price:'))
selling_price = int(input('Enter the selling price:'))

if(selling_price > cost_price):
    print("profit=",selling_price-cost_price)
elif(cost_price > selling_price):
    print("loss=",cost_price-selling_price)
else:
    print("No profit no loss")