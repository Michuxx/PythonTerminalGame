import classes.mainCharacter.mainCharacterClass as char
import town.town as city
import os

os.system('cls')

heroName = input("Wprowadź nazwę gracza: ")

hero = char.Character(heroName)

city.enterTown()
