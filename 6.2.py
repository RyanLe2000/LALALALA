def main():
    number_count = 0
    number_total = 0
    numbers_file = open('numbers.txt', 'r')
    nrecord = numbers_file.readline()
    nrecord = nrecord.strip('\n')
    while nrecord != "":
        nrecord = int(nrecord)
        for x in numbers_file:
            number_count += 1
    print(nrecord)
    print('there is', nrecord, 'numbers')
    numbers_file.close()
main()
