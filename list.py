from item import Item

class ListOfItems:

    def __init__(self):
    
        self.list = []
        
    def add_item(self, name, description):
    
        self.list.append(Item(name, description))
        
    def del_item(self, name):
    
        self.list.remove(name)
        
    def __str__(self):
    
        string = ''
        index = 1
        
        for item in self.list:
            string += str(index) + ') ' + item.__str__(False) + '\n'
            index += 1
            
        return string
