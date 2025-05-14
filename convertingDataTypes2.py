# Task:
# Create a solution that accepts an integer input representing a 9-digit unformatted student identification number.
# Output the identification number as a string with no spaces.
# The solution output should be in the format
# 111-22-3333
#
# Sample Input/Output:
# If the input is
# 154175430
# then the expected output is
# 154-17-5430

student_id = int(input())

student_ids = str(student_id)

first_three = student_ids[0:3]
mid_two = student_ids[3:5]
last_four = student_ids[5:9]

new_student_id = first_three + '-' + mid_two + '-' + last_four

print(new_student_id)