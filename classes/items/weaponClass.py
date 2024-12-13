class Weapon:
    def __init__(self, minAttack, maxAttack, name, materials):
        self.minAttack = minAttack
        self.maxAttack = maxAttack
        self.name = name
        self.materials = materials
    upgrade = 0
    isEquipped = False
    itemType = "weapon"

    def updateStatistics(self):
        self.minAttack += 2
        self.maxAttack += 5

    def upgradeWeapon(self):
        self.upgrade += 1
    
    def increaseAmount(self):
        self.materials.amount += 6

    def howMuchMoreMin(self):
        futureMinAttack = 2 + self.minAttack
        return futureMinAttack
    
    def howMuchMoreMax(self):
        futureMaxAttack = 5 + self.maxAttack
        return futureMaxAttack
    