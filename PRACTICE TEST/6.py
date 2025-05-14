# Task:
# Create a solution that accepts an integer input representing a 9-digit unformatted student identification number. Output the identification number as a string with no spaces.
# The solution output should be in the format
# 111-22-3333
#
# Sample Input/Output:
# If the input is
# 154175430
# then the expected output is
# 154-17-5430

student_id = int(input())

conv_student_id = str(student_id)

print(f'{conv_student_id[0:3]}-{conv_student_id[3:5]}-{conv_student_id[5:]}')