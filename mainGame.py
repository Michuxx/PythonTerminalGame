import classes.mainCharacter.mainCharacterClass as char

heroName = input("Wprowadź nazwę gracza: ")

hero = char.Character(heroName)

print(hero.name)
