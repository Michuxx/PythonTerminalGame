import os

def enterTown():
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
            print("jesteś w postaci")
        case "3":
            os.system('cls')
            print("jesteś w plecaku")
        case "4":
            os.system('cls')
            print("jesteś w expowisko")
        case _:
            os.system('cls')
            print("Nieprawidłowa opcja... Wybierz jeszcze raz")
            enterTown()