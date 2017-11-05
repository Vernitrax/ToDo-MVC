from view import *
from list import ListOfItems

def main():

    list_of_items = ListOfItems()

    while True:
    
        display_options()
        inp = select_option()
        if inp == '1':
            add_item(list_of_items)
        elif inp == '2':
            modify_item(list_of_items)
        elif inp == '3':
            delete_item(list_of_items)
        elif inp == '4':
            mark_item(list_of_items)
        elif inp == '5':
            display_list(list_of_items)
        elif inp == '6':
            display_details(list_of_items)
        else
            break

if __name__ == '__main__':
    main()
