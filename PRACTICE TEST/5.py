# Task:
# Create a solution that accepts five integer inputs. Output the sum of the five inputs three times, converting the inputs to the requested data type prior to finding the sum.
# First output: sum of five inputs maintained as integer values
# Second output: sum of five inputs converted to float values
# Third output: sum of five inputs converted to string values (concatenate)
# The solution output should be in the format
# Integer: integer_sum_value Float: float_sum_value String: string_sum_value
#
# Sample Input/Output:
# If the input is
# 1
# 3
# 6
# 2
# 7
# then the expected output is
# Integer: 19
# Float: 19.0
# String: 13627


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

int_sum = a + b + c + d + e
flt_sum = float(a + b + c + d + e)
str_sum = str(a) + str(b) + str(c) + str(d) + str(e)


print(f'Integer: {int_sum}')
print(f'Float: {flt_sum}')
print(f'String: {str_sum}')