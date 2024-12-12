import os
def showStatistics(hero):

    from town.town import enterTown


    print("---------------------------------------------")
    print("-----------------\033[95mSTATYSTYKI\033[0m------------------")
    print("---------------------------------------------")
    print(f"| \033[4mImię\033[0m: \033[1m{hero.name}\033[0m")
    print(f"| \033[4m\033[91mŻycie\033[0m: \033[91m{hero.health}\033[0m")
    print(f"| \033[4m\033[36mObrona\033[0m: \033[36m{hero.defense}\033[0m")
    print(f"| \033[4m\033[92mAtak\033[0m: \033[92m{hero.attack}\033[0m")
    print(f"| \033[4m\033[96mLevel\033[0m: \033[96m{hero.level}\033[0m")
    print(f"| \033[4m\033[93mExp\033[0m: \033[93m{hero.exp}\033[0m / \033[93m{hero.toLevelUpExp}\033[0m")
    print("---------------------------------------------")
    if hero.weapon != None:
        print(f"| \033[4m\033[94mBroń\033[0m: \033[94m{hero.weapon.name}\033[0m +{hero.weapon.upgrade} | Obrażenia: \033[91m{hero.weapon.minAttack}\033[0m - \033[91m{hero.weapon.maxAttack}\033[0m")
    else:
        print(f"| \033[4m\033[94mBroń\033[0m: Brak\033[0m")
    if hero.helmet != None:
        print(f"| \033[4m\033[96mHełm\033[0m: \033[96m{hero.helmet.name}\033[0m +{hero.helmet.upgrade} | Obrona: \033[36m{hero.helmet.defense}\033[0m")
    else:
        print(f"| \033[4m\033[96mHełm\033[0m: Brak")
    if hero.chest != None:
        print(f"| \033[4m\033[95mNapierśnik\033[0m: \033[95m{hero.chest.name}\033[0m +{hero.chest.upgrade} | Obrona: \033[36m{hero.chest.defense}\033[0m")
    else:
        print(f"| \033[4m\033[95mNapierśnik\033[0m: Brak")
    if hero.leggings != None:
        print(f"| \033[4m\033[93mNogawice\033[0m: \033[93m{hero.leggings.name}\033[0m +{hero.leggings.upgrade} | Obrona: \033[36m{hero.leggings.defense}\033[0m")
    else:
        print(f"| \033[4m\033[93mNogawice\033[0m: Brak")
    print("---------------------------------------------")
    print("| \033[4m\033[33mX. Wróć\033[0m -----------------------------------")
    print("---------------------------------------------")
    statisticChoice = input()
    match statisticChoice:
        case "x":
            os.system('cls')
            enterTown(hero)
        case _:
            os.system('cls')
            print("\033[31mNieprawidłowa opcja... Wybierz jeszcze raz\033[0m")
            showStatistics(hero)