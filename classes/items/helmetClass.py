class Helmet:
    def __init__(self, defense, name, materials):
        self.defense = defense
        self.name = name
        self.materials = materials
    upgrade = 0
    isEquipped = False
    itemType = "helmet"

    def updateStatistics(self):
        self.defense += 1

    def upgradeHelmet(self):
        self.upgrade += 1

    def increaseAmount(self):
        self.materials.amount += 6
    
    def howMuchMore(self):
        return 3+ self.defense