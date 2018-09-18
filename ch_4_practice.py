"""
	Complete all of the TODO directions
	The number next to the TODO represents the chapter
    and section that explain the required code
	Your file should compile error free
	Submit your completed file
"""
# TODO 4.2 A condition controlled loop
# write a loop that will change the variable in num by subtracting 1
# then print the variable. Keep looping until the num = 0 (While num > 0)

# write your code here, the variable needs to exist before
# you test it

num = 10
while num > -1:
  print(num)
  num -= 1

# TODO 4.3 the For Loop
# Use a for loop with a list of the days of the week, print each day
# of the week

days = ["monday", "tuesday", "wensday", "thursday", "friday", 'saturday', 'sunday']
for x in days:
  print(x)

# TODO 4.3 the for loop - range function
# use the range function to print the numbers from 1 to 10

for x in range(11):
  print(x)

# TODO 4.4 a running total
# Have the user enter 5 numbers, provide a total at the end
# You can assume integers

user_total = 0

for user_num in range (0, 5):
    n_num = int(input('Enter a number '))
    user_total += user_num
    print(user_total)

# TODO 4.5 Sentinel Value
# Create a variable to store a total amount
# Create a variable to store a count of the numbers entered
# Have the user enter test scores until a sentinel value of -1 is
# entered.
# Display the total, the count and the a10
# verage (total / count)

tax = 0
rec = 0
soul = 0
while soul != - 1:
    soul = int(input('Enter the test scores, -1 to finish '))
if soul != -1:
    rec += 1
    tax += soul

    print('you put: ' + str(rec) + ' numbers')
print('the total of all scores is: ' + str(tax))

average = tax / rec
print('the average: ' + format(average, ',.2f'))
# TODO 4.6 validating data
# Ask the user to enter a number between 1 and 10.
# Use a while loop to force the user to repeat the
# prompt until the user enters a valid number. Test with
# both valid and invalid data

put = int(input('Enter a number between 1 - 10 '))
while put > 5 or put < 5:
    print('Invalid, please try again ')
    put = int(input('Enter a number between 1 - 10 '))
if put is 5:
    print('you good')
