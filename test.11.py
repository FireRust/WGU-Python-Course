# Task:
# Create a solution that accepts a string input representing a grocery store item and an integer input identifying the number of items purchased on a recent visit.
#
# The following dictionary purchase lists available items as the key with the cost per item as the value.
#
# purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}
#
# Additionally,
# If fewer than ten items are purchased, the price is the full cost per item.
# If between ten and twenty items (inclusive) are purchased, the purchase gets a 5% discount.
# If twenty-one or more items are purchased, the purchase gets a 10% discount.
# Output the chosen item and total cost of the purchase to two decimal places.
# The solution output should be in the format
# item_purchased $total_purchase_cost
#
# Sample Input/Output:
# If the input is
# bananas
# 12
# then the expected output is
# bananas $21.09
# Alternatively, if the input is
# cookies
# 144
# then the expected output is
# cookies $585.79

purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

grocery_store_item = input()
num_items_purchased = int(input())

discount = 0
total_price = purchase.get(grocery_store_item) * num_items_purchased

if num_items_purchased < 10:
    discount = 0
elif num_items_purchased <= 20:
    discount = (total_price * 0.05)
elif num_items_purchased >= 21:
    discount = (total_price * 0.10)


if discount > 0:
    print(f'{grocery_store_item} ${total_price - discount:.2f}')
else:
    print(f'{grocery_store_item} ${total_price:.2f}')


