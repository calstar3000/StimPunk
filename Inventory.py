class Inventory(object):
    '''Defines the player's inventory'''
    
    def __init__(self, weapons=[], ammo=0):
        '''Creates a new inventory'''
        self.weapons = weapons
        self.ammo = ammo
        
    def description(self):
        '''Return a description of the inventory'''
        description = ''
        
        for i in range(len(self.weapons)):
            description += "Weapon {0}:\n".format(i+1)
            description += "  {0}\n".format(self.weapons[i].description())
    
        return description
    
    def addWeapon(self, weapon):
        '''Add a weapon to the inventory'''
        self.weapons.append(weapon)
        
    def addWeapons(self, weapons):
        '''Add weapons to the inventory'''
        self.weapons.extend(weapons)
        
    def removeWeapon(self, weapon):
        '''Remove a weapon from the inventory'''
        if weapon not in self.weapons:
            print("Weapon is not in the inventory")
        else:    
            self.weapons.remove(weapon)         
            