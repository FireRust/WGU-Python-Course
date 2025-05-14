# Driving is expensive. Write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.
#
# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')
#
# Ex: If the input is:
#
# 20.0
# 3.1599
# where the gas mileage is 20.0 miles/gallon and the cost of gas is $3.1599/gallon, the output is:
#
# 3.16 11.85 79.00
# Note: Real per-mile cost would also include maintenance and depreciation.

miles_per_gallon = float(input())
dollars_per_gallon = float(input())

num1 = (20 / miles_per_gallon) * dollars_per_gallon
num2 = (75 / miles_per_gallon) * dollars_per_gallon
num3 = (500 / miles_per_gallon) * dollars_per_gallon

print(f'{num1:.2f} {num2:.2f} {num3:.2f}')