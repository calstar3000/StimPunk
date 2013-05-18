class Weapon:
    '''Defines a weapon'''
    
    def __init__(self, name, price, weaponType, ammoType, numRounds):
        self.name = name
        self.price = price
        self.weaponType = weaponType
        self.numRounds = numRounds
        self.ammoType = ammoType
    
    @property
    def name(self):
        '''Get the weapons's name'''
        return self._name
    
    @name.setter
    def name(self, value):
        '''Set the weapon's name'''
        self._name = value
        
    @property
    def price(self):
        '''Get the weapons's price'''
        return self._name
    
    @price.setter
    def price(self, value):
        '''Set the weapon's price'''
        self._price = value
        
    @property
    def weaponType(self):
        '''Get the weapons's type'''
        return self._weaponType
    
    @weaponType.setter
    def weaponType(self, value):
        '''Set the weapon's type'''
        self._weaponType = value
        
    @property
    def numRounds(self):
        '''Get the weapons's number of rounds per clip'''
        return self._numRounds
    
    @numRounds.setter
    def numRounds(self, value):
        '''Set the weapon's number of rounds per clip'''
        self._numRounds = value
        
    @property
    def ammoType(self):
        '''Get the weapons's ammo type'''
        return self._ammoType
    
    @ammoType.setter
    def ammoType(self, value):
        '''Set the weapon's ammo type'''
        self._ammoType = value
    
    def description(self):
        return '''Name:  {0}
  Price:  {1}
  Type:   {2}
  Rounds: {3}
  Ammo:   {4}'''.format(self._name, self._price, self._weaponType, 
                        self._numRounds, self._ammoType)
