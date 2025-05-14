# (1) Prompt the user to enter a string of their choosing. Output the string. (1 pt)
#
# Ex:
#
# Enter a sentence or phrase:
# The only thing we have to fear is fear itself.
#
# You entered: The only thing we have to fear is fear itself.
# (2) Complete the get_num_of_characters() function, which returns the number of characters in the user('s string. '
# We encourage you to use a for loop in this function. (2 pts))
#
# (3) Extend the program by calling the get_num_of_characters() function and then output the returned result. (1 pt)
#
# (4) Extend the program further by implementing the output_without_whitespace() function.
# output_without_whitespace() outputs the string('s characters except for whitespace (spaces, tabs).
# Note: A tab is ')\t'. Call the output_without_whitespace() function in main(). (2 pts)
#
# Ex:
#
# Enter a sentence or phrase:
# The only thing we have to fear is fear itself.
#
# You entered: The only thing we have to fear is fear itself.
#
# Number of characters: 46
# String with no whitespace: Theonlythingwehavetofearisfearitself.



def get_num_of_characters(num):
    count = 0
    for i in num:
        count += 1
    return count

def output_without_whitespace(text):
    new_string = ""
    for char in text:
        if char != " " and char != "\t":
            new_string += char
    return new_string

if __name__ == '__main__':
    user_input = input("Enter a sentence or phrase:\n")
    print(f'\nYou entered: {user_input}\n')
    num_characters = get_num_of_characters(user_input)
    print(f'Number of characters: {num_characters}')
    print(f'String with no whitespace: {output_without_whitespace(user_input)}')