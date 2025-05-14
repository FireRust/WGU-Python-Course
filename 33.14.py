# A palindrome is a word or a phrase that is the same when read both forward and backward.
# Examples are: "bob," "sees," or "never odd or even" (ignoring spaces).
# Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.
#
# Ex: If the input is:
#
# bob
# the output is:
#
# bob is a palindrome
# Ex: If the input is:
#
# bobby
# the output is:
#
# bobby is not a palindrome
# # Hint: Start by removing spaces. Then check if a string is equivalent to it's reverse.


# FIRST ATTEMPT
#
# user_input = input()
#
# new_text = ""
# for char in user_input:
#     if char != " ":
#         new_text += char
#
# text_list = []
# for char in new_text:
#     text_list.append(char)
#
# new_text_list = []
# for char in text_list[::-1]:
#     new_text_list.append(char)
#
# if text_list == new_text_list:
#     print(f'{user_input} is a palindrome')
# else:
#     print(f'{user_input} is not a palindrome')

####### Clean version using '.replace()' #######
user_input = input()

clean_text = user_input.replace(" ", "")

if clean_text == clean_text[::-1]:
    print(f'{user_input} is a palindrome')
else:
    print(f'{user_input} is not a palindrome')
