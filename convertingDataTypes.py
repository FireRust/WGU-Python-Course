# Task:
# Create a solution that accepts five integer inputs.
# Output the sum of the five inputs three times, converting the inputs to the requested data type prior to finding the sum.
#
# First output: sum of five inputs maintained as integer values
# Second output: sum of five inputs converted to float values
# Third output: sum of five inputs converted to string values (concatenate)
#
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

int1 = int(input())
int2 = int(input())
int3 = int(input())
int4 = int(input())
int5 = int(input())

int_output = int1 + int2 + int3 + int4 + int5
flt_output = float(int1) + float(int2) + float(int3) + float(int4) + float(int5)
str_output = str(int1) + str(int2) + str(int3) + str(int4) + str(int5)

print(f'Integer: {int_output}')
print(f'Float: {flt_output}')
print(f'String: {str_output}')