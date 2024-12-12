import os

def enterTown(hero):
    from charStatistics.statistics import showStatistics
    from backpack.inventory import enterBackpack
    print("----------------------------------")
    print("-------------MIASTO---------------")
    print("----------------------------------")
    print("| 1. Kampania --------------------")
    print("| 2. postac ----------------------")
    print("| 3. plecak ----------------------")
    print("| 4. expowisko -------------------")
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
            print("jesteś w expowisko")
        case _:
            os.system('cls')
            print("Nieprawidłowa opcja... Wybierz jeszcze raz")
            enterTown()