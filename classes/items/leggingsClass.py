class Leggings:
    def __init__(self, defense, name, materials):
        self.defense = defense
        self.name = name
        self.materials = materials
    upgrade = 0
    isEquipped = False
    itemType = "leggings"

    def updateStatistics(self):
        self.defense += 3

    def upgradeLeggings(self):
        self.upgrade += 1
        self.materials.amount += 6