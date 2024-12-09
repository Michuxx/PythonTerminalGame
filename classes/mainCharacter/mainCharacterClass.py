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

        helm_def = self.helmet.defense if self.helmet is not None else 0
        chest_def = self.chest.defense if self.chest is not None else 0
        legs_def = self.leggings.defense if self.leggings is not None else 0

        self.defense = helm_def + chest_def + legs_def
        
        self.backpack = [weaponItem.stoneSword, weaponItem.woodenSword, leggingsItem.skinLegs, 
                         leggingsItem.ironLegs, helmetsItem.skinHelmet, helmetsItem.ironHelmet, 
                         chestsItem.skinChest, chestsItem.ironChest]
        
        self.attack = 5 + self.level
        self.campaignLevel = 1
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