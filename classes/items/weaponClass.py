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
        self.materials.amount += 6
    