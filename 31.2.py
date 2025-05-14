# Write a program that reads movie data from a CSV (comma separated values) file and output the data in a formatted table.
# The program first reads the name of the CSV file from the user.
# The program then reads the CSV file and outputs the contents according to the following requirements:
#
# Each row contains the title, rating, and all showtimes of a unique movie.
# A space is placed before and after each vertical separator ('|') in each row.
# Column 1 displays the movie titles and is left justified with a minimum of 44 characters.
# If the movie title has more than 44 characters, output the first 44 characters only.
# Column 2 displays the movie ratings and is right justified with a minimum of 5 characters.
# Column 3 displays all the showtimes of the same movie, separated by a space.
# Each row of the CSV file contains the showtime, title, and rating of a movie. Assume data of the same movie are grouped in consecutive rows.
#
# Ex: If the input of the program is:
#
# movies.csv
# and the contents of movies.csv are:
#
# 16:40,Wonders of the World,G
# 20:00,Wonders of the World,G
# 19:00,Journey to Space,PG-13
# 12:45,Buffalo Bill And The Indians or Sitting Bull's History Lesson,PG
# 15:00,Buffalo Bill And The Indians or Sitting Bull's History Lesson,PG
# 19:30,Buffalo Bill And The Indians or Sitting Bull's History Lesson,PG
# 10:00,Adventure of Lewis and Clark,PG-13
# 14:30,Adventure of Lewis and Clark,PG-13
# 19:00,Halloween,R
# the output of the program is:
#
# Wonders of the World                         |     G | 16:40 20:00
# Journey to Space                             | PG-13 | 19:00
# Buffalo Bill And The Indians or Sitting Bull |    PG | 12:45 15:00 19:30
# Adventure of Lewis and Clark                 | PG-13 | 10:00 14:30
# Halloween                                    |     R | 19:00

file_name = input()

movies = {}

with open(file_name, 'r') as file:
    for line in file:
        showtime, title, rating = line.strip().split(',')

        if title not in movies:
            movies[title] = {'rating': rating, 'showtimes': [showtime]}
        else:
            movies[title]['showtimes'].append(showtime)

print()
for title, data in movies.items():