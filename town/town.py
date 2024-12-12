import os

def enterTown(hero):
    from charStatistics.statistics import showStatistics
    from backpack.inventory import enterBackpack
    from blacksmith.blacksmith import enterBlacksmith
    print("----------------------------------")
    print("-------------MIASTO---------------")
    print("----------------------------------")
    print("| 1. Kampania --------------------")
    print("| \033[95m2. Postac\033[0m ----------------------")
    print("| \033[92m3. Plecak\033[0m ----------------------")
    print("| \033[33m4. Kowal\033[0m -----------------------")
    print("| 5. Expowisko -------------------")
    print("----------------------------------")
    choice = input()
    match choice:
        case "1":
            os.system('cls')
            print("jesteś w kampanii")
        case "2":
            os.system('cls')
            showStatistics(hero)
        case "3":
            os.system('cls')
            enterBackpack(hero)
        case "4":
            os.system('cls')
            enterBlacksmith(hero)
        case "5":
            os.system('cls')
            print("jesteś w expowisko")
        case _:
            os.system('cls')
            print("\033[31mNieprawidłowa opcja... Wybierz jeszcze raz\033[0m")
            enterTown(hero)