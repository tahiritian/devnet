class Player:
    health = 10
    revives = 3

    def revive(self):
        if self.health >= 0:
            print("Player has health, they do not need to be revived!")
            return
        elif self.revives <= 0:
            print("This player is out of revives, sorry :(")
            return

        self.revives = self.revives - 1
        self.health = 10        

player1 = Player()
player2 = Player()

player1.revive()
player2.revive()