import items.weapons.weapons as weaponItem
import items.leggings.leggings as leggingsItem
import items.helmets.helmets as helmetsItem
import items.chests.chests as chestsItem

class Character:
    def __init__(self, name):
        self.name = name
        self.exp = 0
        self.level = 1
        self.toLevelUpExp = 200 + self.level * 100
        self.health = 50 + self.level * 15
        self.weapon = None

        self.helmet = None
        self.chest = None
        self.leggings = None

        # helm_def = self.helmet.defense if self.helmet is not None else 0
        # chest_def = self.chest.defense if self.chest is not None else 0
        # legs_def = self.leggings.defense if self.leggings is not None else 0

        self.defense = 0
        
        self.backpack = [weaponItem.stoneSword, weaponItem.woodenSword, leggingsItem.skinLegs, 
                         leggingsItem.ironLegs, helmetsItem.skinHelmet, helmetsItem.ironHelmet, 
                         chestsItem.skinChest, chestsItem.ironChest]
        self.attack = 5 + self.level
        self.campaignLevel = 1

    def updateDefense(self):
        helm_def = self.helmet.defense if self.helmet else 0
        chest_def = self.chest.defense if self.chest else 0
        legs_def = self.leggings.defense if self.leggings else 0
        self.defense = helm_def + chest_def + legs_def

    def equipWeapon(self, weapon):
        self.weapon = weapon
        weapon.isEquipped = True

    def takeOffWeapon(self, weapon):
        self.weapon = None
        weapon.isEquipped = False

    def replaceWeapon(self, newWeapon, oldWeapon):
        oldWeapon.isEquipped = False
        newWeapon.isEquipped = True
        self.weapon = newWeapon

    def deleteWeapon(self, weapon):
        if self.weapon == weapon:
            self.weapon = None
        filteredBackpack = filter(lambda item: item is not weapon, self.backpack)
        self.backpack = list(filteredBackpack)

    def equipHelmet(self, helmet):
        self.helmet = helmet
        helmet.isEquipped = True

    def takeOffHelmet(self, helmet):
        self.Helmet = None
        helmet.isEquipped = False

    def replaceHelmet(self, newHelmet, oldHelmet):
        oldHelmet.isEquipped = False
        newHelmet.isEquipped = True
        self.Helmet = newHelmet

    def deleteHelmet(self, helmet):
        if self.Helmet == helmet:
            self.Helmet = None
        filteredBackpack = filter(lambda item: item is not helmet, self.backpack)
        self.backpack = list(filteredBackpack)

    def equipChest(self, chest):
        self.chest = chest
        chest.isEquipped = True

    def takeOffChest(self, chest):
        self.chest = None
        chest.isEquipped = False

    def replaceChest(self, newChest, oldChest):
        oldChest.isEquipped = False
        newChest.isEquipped = True
        self.chest = newChest

    def deleteChest(self, chest):
        if self.chest == chest:
            self.chest = None
        filteredBackpack = filter(lambda item: item is not chest, self.backpack)
        self.backpack = list(filteredBackpack)

    def equipLeggings(self, leggings):
        self.leggings = leggings
        leggings.isEquipped = True
        
    def takeOffLeggings(self, leggings):
        self.leggings = None
        leggings.isEquipped = False

    def replaceLeggings(self, newLeggings, oldLeggings):
        oldLeggings.isEquipped = False
        newLeggings.isEquipped = True
        self.leggings = newLeggings

    def deleteLeggings(self, leggings):
        if self.leggings == leggings:
            self.leggings = None
        filteredBackpack = filter(lambda item: item is not leggings, self.backpack)
        self.backpack = list(filteredBackpack)