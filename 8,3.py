
common = ''
for char in user_string
    if let_count > old_count
    old_count = let_count
    common = char
elif let_count == old_count
common = common + " " + char


Write a program that lets the user enter a string and displays the letter that appears most frequently in the string.
Ignore spaces, punctuation, and uppercase vs lowercase.



Hints:

Create a list to hold letters based on the length of the user input
Convert all letters to the same case
Use a loop to check for each letter in the alphabet (create an alphabet list and step through it)
Have a variable to hold the largest number of times a letter appears, and replace the value when a higher number is found



Please enter a phrase: Narwhals Narwhals swimming in the ocean
The most common letter(s):
A N appeared 5 times.
