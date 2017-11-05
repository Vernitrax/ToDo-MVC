class Item:

    def __init__(self, name, description):
    
        self.name = name
        self.description = description
        self.is_done = False
        
    def modify_name(self, new_name):
    
        self.name = new_name
        
    def modify_description(self, new_description):
    
        self.description = new_description
        
    def mark_as_done(self):
    
        self.is_done = True
