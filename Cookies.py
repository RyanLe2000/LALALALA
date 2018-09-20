butter_total = 48 / 1
sugar_total = 48 /1.5
flour_total = 48 / 2.75

print('you can make 48 cookies with the following ingredients: ')
print(format(butter_total, ',.2f') + " cups of butter")
print(format(sugar_total, ',.2f') + " cups of sugar")
print(format(flour_total, ',.2f') + " cups of flour")

cookie = int(input('How many cookies do you want?'))

butter_total = cookie/1
sugar_total = cookie/1.5
flour_total = cookie/2.75

print("you can make " , cookie , " cookies with the following")

print(format(butter_total, ',.2f') + " cups of butter")
print(format(sugar_total, ',.2f') + " cups of sugar")
print(format(flour_total, ',.2f') + " cups of flour")
