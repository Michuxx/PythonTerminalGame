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
    if hero.weapon != None:
        print(f"| Broń: {hero.weapon.name}")
    else:
        print(f"| Broń: Brak")
    if hero.helmet != None:
        print(f"| Hełm: {hero.helmet.name}")
    else:
        print(f"| Hełm: Brak")
    if hero.chest != None:
        print(f"| Napierśnik: {hero.chest.name}")
    else:
        print(f"| Napierśnik: Brak")
    if hero.leggings != None:
        print(f"| Nogawice: {hero.leggings.name}")
    else:
        print(f"| Nogawice: Brak")
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
            showStatistics(hero)