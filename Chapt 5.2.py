def main():
    fat_total =  calc_fat()
    print("you ate " + str(fat_total) + ' calories in fat')
    carbs_total = calc_carbs()
    print('you ate ' + str(carbs_total) + " in carbs")
    prot_total = calc_prot()
    print('you ate ' + str(prot_total) + ' in protien')
    total = (fat_total + carbs_total + prot_total)
    print(" you ate about " + str(total) + " Calories today")

def calc_fat():
    fat_calories = int(input("how many callories you ate "))
    fat_cal = fat_calories * 9
    return fat_cal

def calc_carbs():
    carbs_calories = int(input("how many carbs you ate "))
    carbs_cal = carbs_calories * 4
    return carbs_cal

def calc_prot():
    prot_calories = int(input("how many prot you ate "))
    prot_cal = prot_calories * 4
    return prot_cal
main()
