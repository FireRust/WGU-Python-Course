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

emp_a = int(input())
emp_b = int(input())
emp_c = int(input())

a_miles = emp_a * 15.62
b_miles = emp_b * 41.85
c_miles = emp_c * 32.67

total_miles_traveled = a_miles + b_miles + c_miles

print(f'Distance: {total_miles_traveled:.2f} miles')