from list import ListOfItems

def display_options():
    print('''
Choose what to do, type 1-6 or q to quit:
    1) Add new item to the list
    2) Modify existing item
    3) Delete item
    4) Mark item as done
    5) Display all items
    6) Display details of item
    ''')
    
    
def select_option():
    while True:
        inp = input()
        if inp in '123456q' and len(inp) == 1:
            return inp
        print('Wrong input!')
    
def add_item(list_of_items):
    print('Adding new item...')
    while True:
        inp = input('Choose name for new item, max 20 characters ')
        if len(inp) < 21:
            name = inp
            break
        print('Too long!')
    while True:
        inp = input('Choose description for new item, max 150 characters ')
        if len(inp) < 151:
            description = inp
            break
        print('Too long!')
    list_of_items.add_item(name, description)
    
def modify_item(list_of_items):
    while True:
        print(list_of_items)
        inp = input('Which item you want to modify? ')
        if inp.isdigit():
            if int(inp) > len(list_of_items.list) and not inp == '0':
                print('There is no such item!')
                continue
            index = int(inp) - 1
            break
    while True:
        inp = input('You want to modify name(n) or description(d)? ')
        if inp == 'd' or inp == 'n':
            mode = inp
            break
        print('Choose n or d!')
    if mode == 'n':
        while True:
            inp = input ('Choose new name for item, max 20 characters ')
            if len(inp) < 21:
                name = inp
                break
            print('Too long!')
        list_of_items.list[index].modify_name(name)
    else:
        while True:
            inp = input ('Choose new description for item, max 150 characters ')
            if len(inp) < 151:
                description = inp
                break
            print('Too long!')
        list_of_items.list[index].modify_description(description)
    
def delete_item(list_of_items):
    while True:
        print(list_of_items)
        inp = input('Which item you want to delete? ')
        if inp.isdigit():
            if int(inp) > len(list_of_items.list) and not inp == '0':
                print('There is no such item!')
                continue
            index = int(inp) - 1
            break
    list_of_items.del_item(list_of_items.list[index].name)
    
def mark_item(list_of_items):
    while True:
        print(list_of_items)
        inp = input('Which item you want to mark as completed? ')
        if inp.isdigit():
            if int(inp) > len(list_of_items.list) and not inp == '0':
                print('There is no such item!')
                continue
            index = int(inp) - 1
            break
    list_of_items.list[index].mark_as_done()
    
def display_list(list_of_items):
    print('List:')
    print(list_of_items)
    
def display_details(list_of_items):
    while True:
        print(list_of_items)
        inp = input('Which item details you want to see? ')
        if inp.isdigit():
            if int(inp) > len(list_of_items.list) and not inp == '0':
                print('There is no such item!')
                continue
            index = int(inp) - 1
            break
    print(list_of_items.list[index].__str__(True))

