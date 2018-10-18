"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""
# TODO 9.1 Dictionaries
# Finish creating the following dictionary by adding three more people and birthdays
birthdays = {'Meri': 'May 16', 'Kathy': 'July 14'}

# 1.Print Meri's Birthday
print(birthdays['Meri'])
# 2.Create an empty dictionary named registration
registration = {}
# 3.You will use the following dictionary for many of the remaining exercises

miles_ridden = {'June 1': 25, 'June 2': 20, 'June 3': 38, 'June 4': 12, 'June 5': 30, 'June 7': 25}

# print the keys and the values of miles_ridden using a for loop
for x in miles_ridden:
    print(x)
# get the value for June 3 and print it, if not found display 'Entry not found', replace the ""
if 'June 3' in miles_ridden:
    print('25')
else:
    print('Entry not found')

# get the value for June 6 and print it, if not found display 'Entry not found' replace the ""
if 'June 6' in miles_ridden:
    print('25')
else:
    print('Entry not found')
# Use the items method to print the miles_ridden dictionary
print(len(miles_ridden))
# Use the keys method to print all of the keys in miles_ridden
for x in miles_ridden:
    print(x)
# Use the pop method to remove june 4 then print the contents of the dictionary
x = miles_ridden.pop('June 4')

print(miles_ridden)
# Use the values method to print the contents of the miles_ridden dictionary
print(miles_ridden)
# TODO 9.2 Sets
# Create an empty set named my_set
my_set = {}
# Create a set named days that contains the days of the week
days = {"Saturday", "Monday", "Tuesday", "Wensday", "Thursday", "Friday", "Sunday"}

# get the number of elements from the days set and print it
print(len(days))
# Remove Saturday and Sunday from the days set
days.discard("Saturday")
days.discard("Sunday")
# Determine if 'Mon' is in the days set
if "Mon" in days:
    print("Mon exists")
else:
    print("Mon doesnt exist")
# TODO 9.3 Serializing Objects (Pickling)

# import the pickle library
import pickle
# create the output file log and open it for binary writing
outputfile = open('mydata.dat', 'wb')
# pickle the miles_ridden dictionary and output it to the log file
pickle.dump(object, outputfile)
# close the log file
outputfile.close()
