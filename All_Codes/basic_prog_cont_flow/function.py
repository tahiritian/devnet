
def revivePlayer(p):
    if p.health >= 0:
        print("Player has health, they do not need to be revived!")
        return
    elif p.revives <= 0:
        print("This player is out of revives, sorry :(")
        return

    p.revives = p.revives - 1
    p.health = 10


revivePlayer(player1)