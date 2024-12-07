from classes.mainCharacter.mainCharacterClass import Character
from game_state import hero
import os

if __name__ == "__main__":
    import town.town as city
    os.system('cls')
    heroName = input("Wprowadź nazwę gracza: ")
    hero = Character(heroName)
    city.enterTown(hero)
