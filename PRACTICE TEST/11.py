# Task:
# Create a solution that accepts a string input representing a grocery store item and an integer input identifying the number of items purchased on a recent visit.
# The following dictionary purchase lists available items as the key with the cost per item as the value.
# purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}
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

store_item = input()
num_items = int(input())

purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

if num_items < 10:
    discount = 0
elif num_items <= 20:
    discount = 0.05
elif num_items > 20:
    discount = 0.10

total_discount = purchase.get(store_item) * num_items * discount
total_cost = purchase.get(store_item) * num_items - total_discount

print(f'{store_item} ${total_cost:.2f}')