import os

def enterBackpack(hero):
    from town.town import enterTown
    print("---------------------------------------------")
    print("-------------------Plecak--------------------")
    print("---------------------------------------------")
    for index, item in enumerate(hero.backpack, start=1):
        print(f"| {index}. {item.name} | Obrażenia: {item.minAttack} - {item.maxAttack} ")
    print("---------------------------------------------")
    print("| X. Wróć -----------------------------------")
    print("---------------------------------------------")
    choice = input()
    match choice:
        case "x":
            os.system('cls')
            enterTown(hero)