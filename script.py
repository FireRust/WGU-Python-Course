print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

def tip_calculator(num):
    tip = num / 100 * bill + bill
    return tip

total_split = (tip_calculator(tip_percentage)) / num_people

print(f'Each person should pay: ${total_split:.2f}')