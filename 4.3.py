num_year = int(input("hopw many years do you wish? "))
for year in range(num_year):
    print('year number ', year + 1)
    total = 0
    for rain in range(1, 6):
        print('rain number ', rain)
        current_rain = int(input('what is he rain '))
        total += current_rain
    print('the average rain ', year + 1, 'ist ', total/5)
