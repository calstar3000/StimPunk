import Player, Weapon

class Game(object):
        
    def start(self):
        '''Start a game'''
        
        phaser = Weapon.Weapon("Phaser", 100.00, "pistol", "energy", 12)
        shredder = Weapon.Weapon("Shredder", 1000.00, "smg", "9mm", 120)
        weapons = [phaser, shredder]
        
        player = Player.Player("Shadow", 18, weapons)
        player.description()             

if __name__ == "__main__":
    game = Game()
    game.start()