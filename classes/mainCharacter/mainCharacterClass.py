class Character:
    def __init__(self, name):
        self.name = name
    exp = 0
    level = 1
    toLevelUpExp = 200 + level * 100
    health = 50 + level * 15
    defense = 0
    attack = 5 + level
    campaignLevel = 1
    weapon = {}
    helmet = {}
    chest = {}
    leggings = {}
    backpack = {}