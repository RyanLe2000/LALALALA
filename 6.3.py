def main():
    filename = 'numbers1.txt'
try:
    numbers_file = open(filename, 'r')
    record = numbers_file.readline()
    record = record.rstrip('\n')
    while record != "":
        print(record)
        record = numbers_file.readline()
        record = record.rstrip('\n')
        try:
            record = int(record)
        except: ValueError:
        print('this item isnt a number: ')
        print("\t". record)
        break

        numbers_file.close()
        except IOError:
            print('cannot find file: ' + filename)


main()
