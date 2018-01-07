class Menu(object):
       
    def __init__(self, root, data, child):
        self.root = root 
        self.child_ids = child
        self.is_valid = True

    def __str__ (self):
        return str(self.__dict__())

    def __dict__(self):
        result = {}
        result['child'] = self.child_ids
        result['root'] = self.root

        return result

    def is_child(self, parent):
        result = False

        if parent in self.child_ids:
            result = True
        
        return result

    def add_child(self, data):
        self.child_ids.append(data['id'])    
        new_child = data['child_ids']

        for new_child in new_child:
            if not new_child in self.child_ids:
                self.child_ids.append(new_child)

        self.child_ids = list(set(self.child_ids))
        self.is_valid = self.valid(data)
    
   def valid(self, data):
        result = True

        for key in data['child_ids']:
            if key == self.root:
                result = False
            if key in self.child_ids: 
                result = False
        return result

    
    
    
