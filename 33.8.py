# Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line.
# The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies.
# Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.
#
# Ex: If the input is:
#
# 0
# (or less than 0), the output is:
#
# No change
# Ex: If the input is:
#
# 45
# the output is:
#
# 1 Quarter
# 2 Dimes

change = int(input())


if change <= 0:
    print('No change')
else:
    remaining_change = change

    dollars = remaining_change // 100
    remaining_change %= 100

    quarters = remaining_change // 25
    remaining_change %= 25

    dimes = remaining_change // 10
    remaining_change %= 10

    nickels = remaining_change // 5
    remaining_change %= 5

    pennies = remaining_change

if dollars >= 2:
    print(f'{dollars} Dollars')
elif dollars == 1:
    print(f'{dollars} Dollar')

if quarters >= 2:
    print(f'{quarters} Quarters')
elif quarters == 1:
    print(f'{quarters} Quarter')

if dimes >= 2:
    print(f'{dimes} Dimes')
elif dimes == 1:
    print(f'{dimes} Dime')

if nickels == 1:
    print(f'{nickels} Nickel')

if pennies >= 2:
    print(f'{pennies} Pennies')
elif pennies == 1:
    print(f'{pennies} Penny')