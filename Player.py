import AgeException, NameException

class Player(object):
    '''Defines the player'''
    
    def __init__(self, name, age, weapons):
        '''Creates a new player'''
        self.name = name
        self.age = age
        self.weapons = weapons
    
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
    def weapon(self):
        '''Get the player's weapon'''
        return self._weapon
    
    @weapon.setter
    def weapon(self, value):
        '''Set the player's weapon'''
        self._weapon = value
          
    def description(self):
        '''Print the player's description'''  
        print("Name:   {0}".format(self._name))
        print("Age:    {0}".format(self._age))
        
        for i in range(len(self.weapons)):
            print("Weapon {0}:".format(i+1))
            print("  {0}".format(self.weapons[i].description()))
        
        
        
        