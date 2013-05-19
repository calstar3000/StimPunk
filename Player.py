import AgeException, NameException

class Player(object):
    '''Defines the player'''
    
    def __init__(self, name, age, inventory):
        '''Creates a new player'''
        self.name = name
        self.age = age
        self.inventory = inventory
    
    @property
    def name(self):
        '''Get the player's name'''
        return self._name
    
    @name.setter
    def name(self, value):
        '''Set the player's name'''
        
        if value == '':
            raise NameException.NameException("You're name can't be empty")
        
        self._name = value
    
    @property
    def age(self):
        '''Get the player's age'''
        return self._age
    
    @age.setter
    def age(self, value):
        '''Set the player's age'''
         
        if value < 18:
            raise AgeException.AgeException("You must be 18 or over to play!")
         
        self._age = value
        
    @property
    def inventory(self):
        '''Get the player's inventory'''
        return self._inventory
    
    @inventory.setter
    def inventory(self, value):
        '''Set the player's inventory'''
        self._inventory = value
               
    def description(self):
        '''Print the player's description'''  
        print("Name:   {0}".format(self._name))
        print("Age:    {0}".format(self._age))
        print("Inventory:")
        print(self.inventory.description())
        
        
        
        