class Weapon:
    def __init__(self, minAttack, maxAttack, name):
        self.minAttack = minAttack
        self.maxAttack = maxAttack
        self.name = name
    isEquipped = False
    itemType = "weapon"
   