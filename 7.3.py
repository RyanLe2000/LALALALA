#Then, write a program that reads the contents of the two files into two separate lists.
#The user should be able to enter a boy's name or a girl's name. The application should check both lists,
#and then display messages indicating whether the names were among the most popular
#if the name was on one of the lists or that the name was not on the lists of popular names.
def main():
    boy_list = []
    try:
        boy_name = open('BoyNames.txt', 'r')

        for boy in boy_name:
            boy = boy.rstrip('\n')
            boy_list.append

        print(boy_list)
        boy_name.close()

        user_name = input(' enter name boy ')

        if user_name is boy_list:
            print(' thats a pop name')
        else:
            print(' that name doesnt exist ')

    except IOError:
        print('sorry that name isnt here')


main()


def main():
    girl_list = []
    try:
        girl_name = open('GirlNames.txt', 'r')

        for girl in girl_name:
            girl = girl.rstrip('\n')
            girl_list.append

        print(girl_list)
        girl_name.close()

        user_name = input(' enter name girl ')

        if user_name is girl_list:
            print(' thats a pop name')
        else:
            print(' that name doesnt exist ')

    except IOError:
        print('sorry that name isnt here')


main()
