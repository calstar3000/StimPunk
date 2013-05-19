class Weapon:
    '''Defines a weapon'''
    
    def __init__(self, name, price, weaponType, ammoType, numRounds, clipCapacity, isEquipped):
        self.name = name
        self.price = price
        self.weaponType = weaponType
        self.ammoType = ammoType
        self.numRounds = numRounds
        self.clipCapacity = clipCapacity
        self.isEquipped = isEquipped
    
    # start properties
    
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
    
    # end properties
    
    def description(self):
        '''Get a description of the weapon'''
        return '''Name:  {0}
  Price:  {1}
  Type:   {2}
  Rounds: {3}
  Ammo:   {4}'''.format(self._name, self._price, self._weaponType, 
                        self._numRounds, self._ammoType)
  
    def isEquipped(self):
        '''See if a weapon is equiped'''
        return self.isEquipped
    
    def fireWeapon(self):
        '''Fire the weapon if equipped and you have rounds'''
        if self.isEquipped:
            
            if self.numRounds > 0:
                self.numRounds -= 1
                print("Blam!!!")
                
                if self.numRounds <= 0:
                    print("Out of ammo!")
            else:
                print("Out of ammo!")
            
            
        else:
            print("You must equip the {0} first!".format(self.name))
                    
    def reloadWeapon(self, inventory):
        '''Reload a weapon'''
        r = self.numRounds
        c = self.clipCapacity
        a = inventory.ammo
        
        if r >= c:
            print("Clip is full")
        else:
            # reload the weapon.
            # if you don't have enough, top up what you can
            if a > 0:
                if c - r > a:
                    self.numRounds += a
                    print("Reloaded, but you're out of ammo!")
                else:
                    self.numRounds = self.clipCapacity
            else:
                print("You're out of ammo!")
                
            inventory.ammo -= a
    