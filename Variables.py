# Instructions:
# Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

# Task:
# Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site.
# Output the total distance traveled to two decimal places given the following miles per employee commute to the job site.
# Employee A: 15.62 miles
# Employee B: 41.85 miles
# Employee C: 32.67 miles
# The solution output should be in the format
# Distance: total_miles_traveled

# Sample Input/Output:
# If the input is
# 1
# 2
# 3
# then the expected output is
# Distance: 197.33 miles

emp_a = 15.62 * int(input())
emp_b = 41.85 * int(input())
emp_c = 32.67 * int(input())

total_miles_traveled = emp_a + emp_b + emp_c

total_distance = print(f'Distance: {total_miles_traveled:.2f} miles')