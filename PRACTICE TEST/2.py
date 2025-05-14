# Task:
# Create a solution that accepts an integer input representing any number of ounces.
# Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value. There are 16 ounces in a pound and 2,000 pounds in a ton.
# The solution output should be in the format
# Tons: value_1
# Pounds: value_2
# Ounces: value_3
#
# Sample Input/Output:
# If the input is
# 32035
# then the expected output is
# Tons: 1
# Pounds: 2
# Ounces: 3

# ORIGINAL SOLUTION
# num_oz = int(input())
#
# tons = num_oz // 32000
# pounds = (num_oz % 32000) // 16
# ounces = (num_oz % 32000) % 16
#
# print(f'Tons: {tons}')
# print(f'Pounds: {pounds}')
# print(f'Ounces: {ounces}')

num_oz = int(input())

tons = num_oz // 32000
num_oz %= 32000

pounds = num_oz // 16
num_oz %= 16

ounces = num_oz

print(f'Tons: {tons}')
print(f'Pounds: {pounds}')
print(f'Ounces: {ounces}')