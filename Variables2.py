# Instructions:
# Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.
#
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

num_ounces = int(input())

total_tons = num_ounces // 32000
total_pounds = (num_ounces % 32000) // 16
total_ounces = (num_ounces % 32000) % 16

print(f'Tons: {total_tons}')
print(f'Pounds: {total_pounds}')
print(f'Ounces: {total_ounces}')