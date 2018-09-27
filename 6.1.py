names_file = open('names.txt')
line1 = print(names_file.readline())
line2 = print(names_file.readline())
line3 = print(names_file.readline())
line4 = print(names_file.readline())
line5 = print(names_file.readline())
names_file.close()
names_file = open('names.txt')
name_total = 0
for x in names_file:
    name_total += 1

print(name_total, ' names were found')

names_file.close()
