name = input('What is your name?: ')
bid = int(input("What's your bid?: "))
secret_bids = {name: bid}

other_people = input('Are there other people in the room? Type "yes" or "no": ')
if other_people.lower() == 'yes':
    print('\n' * 100)


while other_people == 'yes':
    name = input('What is your name?: ')
    bid = int(input("What's your bid?: "))
    secret_bids[name] = bid
    other_people = input('Are there other people in the room? Type "yes" or "no": ')
    print('\n' * 100)

max_bid = 0
max_bidder = None

for bidder in secret_bids:
    if secret_bids[bidder] > max_bid:
        max_bid = secret_bids[bidder]


print(f'The max bid is: ${max_bid}')