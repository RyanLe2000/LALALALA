cookie_num = int(input('How many cookies do you want to make? '))

butter_amt = float(input('How much butter do you have '))
flour_amt = float(input('How much flour you have '))
sugar_amt = float(input('How much sugar you have '))

butter_total = butter_amt / cookie_num
sugar_total = sugar_amt/ cookie_num
flour_total = flour_amt/ cookie_num

print('you can make ' + str(cookie_num) + ' cookies with the following ingredients: ')
print(str(butter_total) + ' sticks of butter')
print(str(sugar_total) + ' ounces of sugar')
print(str(flour_total) + ' pounds of flour')
