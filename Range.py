import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []

print("Welcome to the PyPassword Generator!")

num_letters = int(input('How many letters would you like in your password?\n'))
num_symbols = int(input('How many symbols would you like?\n'))
num_numbers = int(input('How many numbers would you like?\n'))

for i in range(num_letters):
    password = password_list.append(random.choice(letters))
for i in range(num_symbols):
    password = password_list.append(random.choice(symbols))
for i in range(num_numbers):
    password = password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = password_list

for i in password:
    print(i, end='')
