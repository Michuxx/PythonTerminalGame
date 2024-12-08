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
    print("| X. Wróć ------------------------")
    print("----------------------------------")
    statisticChoice = input()
    match statisticChoice:
        case "x":
            os.system('cls')
            enterTown(hero)
        case _:
            os.system('cls')
            print("Nieprawidłowa opcja... Wybierz jeszcze raz")
            showStatistics()