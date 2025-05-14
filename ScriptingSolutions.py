# Task:
# Create a solution that accepts an integer input to compare against the following list:
# predef_list = [4, -27, 15, 33, -10]
# Output a Boolean value indicating whether the input value is greater than the maximum value from predef_list
# The solution output should be in the format
# Greater Than Max? Boolean_value
#
# Sample Input/Output:
# If the input is
# 20
# then the expected output is
# Greater Than Max? False

predef_list = [4, -27, 15, 33, -10]
user_input = int(input())

boolean_value = user_input > max(predef_list)

print(f'Greater Than Max? {boolean_value}')
