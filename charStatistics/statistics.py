import os
def showStatistics(hero):

    from town.town import enterTown


    print("----------------------------------")
    print("-----------STATYSTYKI-------------")
    print("----------------------------------")
    print(f"| Imię: {hero.name}")
    print(f"| Życie: {hero.health}")
    print(f"| Obrona: {hero.defense}")
    print(f"| Atak: {hero.attack}")
    print(f"| Level: {hero.level}")
    print(f"| Exp: {hero.exp} / {hero.toLevelUpExp}")
    print("----------------------------------")
    print("| 1. Wróć ------------------------")
    print("----------------------------------")
    statisticChoice = input()
    match statisticChoice:
        case "1":
            os.system('cls')
            enterTown(hero)
        case _:
            os.system('cls')
            print("Nieprawidłowa opcja... Wybierz jeszcze raz")
            showStatistics()