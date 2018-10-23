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
    else:
        print("Not a valid move")
        menu()


def get_info():
    # get file, unpickle, store in dictionary
    try:
        customer_file = open('customers.dat', 'rb')
        customers_dictionary = pickle.load(customer_file)
    except FileNotFoundError:
        customers_dictionary = {}
    return customers_dictionary



def menu():
    # display menu
    chosen = 0

    try:
        while chosen < 1 or chosen >2:
            print("----------- Customer Accounts --------------")
            print("1:   Add a new customer")
            print("2:   Quit")
            print("3:   Change ")
            print("4:   Remove ")
            print("5:   Lookup ")

            chosen = int(input("Please enter the number of your selection:"))
            if chosen < 1 or chosen > 5:
                print("Not a valid selection.")
            else:
                if chosen == 1:
                    return "add"
                elif chosen == 2:
                    return "quit"
                elif chosen == 3:
                    return "update"
                elif chosen == 4:
                    return "delete"
                elif chosen == 5:
                    return "look"
    except ValueError:
        print("You need to have a numeric entry from the above list")
        menu()



def lookup(customers_lookup):
    found = False
    name = input("enter customers first name ")
    for key in customers_lookup:
        if customers_lookup[key].upper() == name.upper():
            print(customers_lookup[key] + ": " + key + "\n\n\n")
            found = True
    if not found:
        print(" This person isn't in our registry")

def add(customers_add):
    name = input("enter customers first name ")
    email = input("enter email ")
    customer_add(email) = name
    print((customer_add[email]) + " Added. \n\n\n\n")
    save_file(customer_add)

def change(customers_change):
    change_me = input(" enter email to change: ")
    if change_me = input(customers_change):
        print(customers_change[change_me] + ": " + change_me + "\nWill be changed")
    else:
        print(" cant find him")
    del customers_change[change_me]
    change_first = input("please enter name  ")
    change_email = input("enter email ")
    customer_change[change_first]
    save_file(customer_change)

def delete(customers_delete):
    delete_me = input("enter a character to delete: ")
    if delete_me in customers_delete:
        print(customers_delete[delete_me] + ":  " + delete_me + "\nHas been removed")
    save_file(customers_delete)

def save_file(customers_pickle):
    customers = customers_pickle
    customers_pickle[customers]

    save_file(customers_pickle)
main()
