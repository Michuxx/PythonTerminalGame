class Chest:
    def __init__(self, defense, name, materials):
        self.defense = defense
        self.name = name
        self.materials = materials
    upgrade = 0
    isEquipped = False
    itemType = "chest"

    def updateStatistics(self):
        self.defense += 5

    def upgradeChest(self):
        self.upgrade += 1
    
    def increaseAmount(self):
        self.materials.amount += 6

    def howMuchMore(self):
        return 5 + self.defense