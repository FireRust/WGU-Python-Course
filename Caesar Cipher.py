# def life_in_weeks(age):
#     weeks = (90 - age) * 52
#     return weeks
#
#
# current_age = int(input('Enter your age: '))
# print(f'You have {life_in_weeks(current_age)} left.')

# def greet_with(name, location):
#     print(f'Hello {name}!')
#     print(f'What is it like in {location}?')
#
# greet_with(location='Nowhere', name='Jack Bauer')

true_list = ['t', 'r', 'u', 'e']
love_list = ['l', 'o', 'v', 'e']


def calculate_love_score(name1, name2):
    true_points = 0
    love_points = 0
    for i in name1:
        if i in true_list:
            true_points += 1
        if i in love_list:
            love_points += 1

    for i in name2:
        if i in true_list:
            true_points += 1
        if i in love_list:
            love_points += 1

    print(f'Love Score = {true_points + love_points}')


calculate_love_score(name1='John Brigham Jenkins', name2='Jennifer Anniston')