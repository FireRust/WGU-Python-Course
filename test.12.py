# Task:
# Create a solution that opens a file and combines the words on each line into a sentence.
# Write the sentence string to the end of the text file "WordTextFile1.txt" on a new line.
# Output the new contents of "WordTextFile1.txt". Use the open() function and write(), read() methods to interact with the text file.
# The solution output should be in the format
# WordTextFile1.txt_contents
# sentence
#
# Sample Input/Output:
# If the file content is
# WordTextFile1.txt
# then the expected output is
# cat
# chases
# dog
# cat chases dog

with open('WordTextFile1.txt', 'r') as file:
    words = file.read().splitlines()

sentence = ' '.join(words)

with open('WordTextFile1.txt', 'a') as file:
    file.write('\n' + sentence)

with open('WordTextFile1.txt', 'r') as file:
    content = file.read()

print(content)