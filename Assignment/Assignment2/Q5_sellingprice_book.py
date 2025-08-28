##WAP to calculte selling price of book based on cost price and discount.

cost_price = int(input('Enter the cost price:'))
discount = int(input('Enter the Discount:'))

discount_amount = (discount / 100) * cost_price
selling_price = cost_price - discount_amount

print(f'Selling price of book is:{selling_price}')