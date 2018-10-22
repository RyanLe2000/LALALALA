




Lesson Objective(s):
Write a CRUD - Create, Read, Update, Delete application
Pickle files and save them
Unpickle and save into data structures


Lesson:
Write a program that keeps names and email addresses in a dictionary as key-value pairs. The program should display a
menu that lets the user look up a person's email address, add a new name and email address, change an existing email '
    'address, and delete an existing name and email address. The program should '
  'pickle the dictionary and save it to a file when the user exits the program.'
  ' Each time the program starts, it should retrieve the dictionary from the file '
   'and unpickle it.
import pickle
def main():# declare variables
    customers = get_info()
    choice = menu()
    if choice == "look":
        lookup(customers)
    elif choice == "add":
        add(customers)
    elif choice == "update":
        change(customers)
    elif choice == "remove":
        delete(customers)
    elif choice == "quit":
        save_file(customers)
        else:print("not valid entry")
            menu()
            
            
def get_info():
    # get file, unpickle, store in dictionarytry:
        customer_file = open('customers.dat', 'rb')
        customers_dictionary = pickle.load(customer_file)
    except FileNotFoundError:
        customer_file = open('customers.dat', 'wb')
        customers_dictionary = {}
        customer_file.close()
    return customers_dictionary


def menu():
    # display menu
    chosen = 0
    try:
        while chosen < 1 or chosen >2:
        print("----------- Customer Accounts --------------")
        print("1:   Add a new customer")
        print("2:   Quit")
        chosen = int(input("Please enter the number of your selection:"))
        if chosen < 1 or chosen > 2:
            print("Not a valid selection.")
        else:if chosen == 1:
                return "add"
            elif chosen == 2:return "quit"except ValueError:print("You need to have a numeric entry from the above list")menu()def lookup(customers_lookup):# lookup and display a current customerprint("lookup")def add(customers_add):# add a new customerprint("add")def change(customers_change):# update customer informationprint("change")def delete(customers_delete):# delete a customerprint("delete")def save_file(customers_pickle):# pickle and dump the fileprint("save")main()
