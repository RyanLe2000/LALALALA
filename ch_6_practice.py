
# TODO 6.1 Introduction to File Input and Output
# Assign the variable file_variable to open states.txt in read mode

file_variable = open('states.txt')
for x in file_variable:
  print(x)
print(file_variable.read())
# Close the file

file_variable.close()

# Assign the variable state_capitals to open capitals.txt in write mode.
# Please note, the file does not currently exist, and by opening it in
# write mode you will create it

states = open('state_capitals.txt', 'w')
states.write("Montgomery, Juneau, Phoenix")
print(states)
# Write three state capitals to the file
# There is a list of state capitals here: https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States
# sample
#   state_capitals.write("Alabama, Montgomery\n") - make sure to include the \n as a new line symbol

states.write("Montgomery, Juneau, Phoenix",)

# close the file
states.close()

# TODO reading data in from a file
# Assign the variable states_data to open states.txt in read mode

# read in three lines from the file, assign to the variables below, Remove """   """ to test

states_data = open('states.txt')
line1 = print(states_data.readline())
line2 = print(states_data.readline())
line3 = print(states_data.readline())

# close the file
states_data.close()
# print the three variables

# TODO 6.2 Using loops to process files
# Complete the program below to read in and count all of the entries in the states file

# open the file in read mode
counter = 0
states_file = open('states.txt')
for x in states_file:
  print(x)
  counter += 1
  print(str(counter))

# write a for loop to read in all of the lines, and print them on the screen, add 1 to counter for each line

# close the file
states_file.close()
# TODO 6.3 Processing records

# You are going to finish the program below to write data to a file

# entering book information
books = 3

# open the file books.txt for writing remove the """ """ to test
books_file = open('books.txt', 'w')

# use a for loop to get title and author from the user use the range 1, books + 1
for x in range(books):
  print(x)
  counter += 1
  print(str(counter))
# get the data in the loop
    
# write the data as a record in the loop, make sure to include the \n at the end of the line
    
# close the file
books_file.close()

# TODO 6.4 Exceptions
# In this exercise you will try to open a file that does not exist, capture the error, and display a custom error message

# create a try statement:
superheros_file = open('superheros.txt', 'r')
print(superheros_file.read())
import superheros.txt
if superheros.txt.path.exists("superheros.txt.txt"):
  superheros.txt.remove("superheros.txt.txt")
else:
  print("The file does not exist")
# open the file superheros.txt for reading (we are not writing, it would create the file)

# close the file

# create an except IOError, and a print statement telling the user that the file doesn't exist
