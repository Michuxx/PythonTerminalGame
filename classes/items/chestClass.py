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
        self.materials.amount += 6