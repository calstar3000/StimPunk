import Player, Inventory, Weapon

class Game(object):
        
    def start(self):
        '''Start a game'''
        
        #create some weapons
        phaser = Weapon.Weapon("Phaser", 100.00, "pistol", "energy", 1, 12, True)
        shredder = Weapon.Weapon("Shredder", 1000.00, "smg", "9mm", 120, 120, False)
        weapons = [phaser, shredder]
        
        #create the inventory
        inventory = Inventory.Inventory(weapons=[], ammo=10)
        inventory.addWeapons(weapons)
        
        #create the player
        player = Player.Player("Shadow", 18, inventory)
        player.description()
        
        print(Weapon.Weapon.isEquipped(phaser))
        print(Weapon.Weapon.isEquipped(shredder))
        
        Weapon.Weapon.fireWeapon(phaser)
        Weapon.Weapon.fireWeapon(phaser)
        Weapon.Weapon.reloadWeapon(phaser, inventory)
        
        print("rounds = {0}".format(phaser.numRounds))
        print("ammo = {0}".format(inventory.ammo))
        
if __name__ == "__main__":
    game = Game()
    game.start()