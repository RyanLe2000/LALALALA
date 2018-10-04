"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 7.2 Lists
# Create a list of days of the week, assign it to the variable days, remove """ """ to test

days = ["Monday", "Tuesday", 'Wensday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(days)


# Create a list with 5 items, set them all to 0, use the Repetition Operator ( * )
items = ['bags', 'tags', 'rags', 'snags', 'toothpaste']


# print the contents of your days list using the for operator
for x in days:
    print(x)

# print the list item that holds the value Saturday from the days list by using it's index
print(days[5])

# set the size variable to hold the length of the list days using the len function
print(len(days))
# concatenate the two following lists together, storing the value in list3 - remove the """ """ to test


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = list2 + list1
print(list3)


# TODO 7.3 List Slicing
# Slice the list days to select from Monday through Friday, inclusive, and assign the new list to work_days
# print work_days
slice = days
slice.remove("Saturday")
slice.remove("Sunday")
work_days = slice
print(work_days)


# TODO 7.4 Finding items in Lists with the in Operator
# test to see if "Tue" is in the list days, print yes, Tue is in the list or no, Tue is not in the list

if "Tue" in days:
  print("Yes, 'apple' is in the fruits tuple")
else:
  print('its not on the list')

# TODO 7.5 List Methods and Useful Built-in Functions
# Complete the following code to append the last three months of the year to the list months. Remove
# the """   """ to test, and print the contents of months

months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept"]
months.append('October,'  + "'November,' " + "'December'")
print(months)
print(months[4])
# get the index of "May" from the months list and print it on screen

# sort list3 from the 7.2 exercise and print the results on screen
list3.sort
print(list3)

# reverse the order of list 3
list3.reverse()
print(list3)

# print the maximum item from list 3
print(list3.count)

# TODO 7.6 Copying Lists
# copy the list months to the variable months_of_the_year
# print the values in months_of_the_year

months_of_the_year = months.copy()

# TODO 7.7 Processing lists
# total the values in list3 and print the results
values = list3 + list3
print(list3)

count = list3.count

# open the file states in read mode, read the contents of the file into the list states_list and print the
# contents of states_list on screen
states_list = open("states.txt", "r")
print(states_list.read())

# TODO 7.8 Two-Dimensional Lists
# Create a two dimensional list that has the months of the year and the days in each month during a non leap year
# print the contents of the list

dim_list = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept"]
dem_list =["31","30","28","30","31","30","31","30","28","30","31","30"]
# print just the values for index 3,0 and 3,1
print(dim_list[3], dem_list[0])
print(dim_list[3], dem_list[1])

# TODO 7.9 Tuples
# convert the months list to a tuple
dim_list.change()
