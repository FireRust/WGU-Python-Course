import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

placeholder = ''
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input('\nGuess a letter: ').lower()

display = ''

for letter in chosen_word:
    if letter in guess:
        display += letter
    else:
        display += '_'

print(display)


