import os

def enterBackpack(hero):
    from town.town import enterTown
    print("--------------------------------------------------")
    print("----------------------Plecak----------------------")
    print("--------------------------------------------------")
    for index, item in enumerate(hero.backpack, start=1):
        if item.isEquipped == False:
            print(f"| {index}. {item.name} | Obrażenia: {item.minAttack} - {item.maxAttack} ")
        else:
            print(f"| {index}. {item.name} | Obrażenia: {item.minAttack} - {item.maxAttack} | Założono")
    print("--------------------------------------------------")
    print("| Wybierz przedmiot ------------------------------")
    print("| X. Wróć ----------------------------------------")
    print("--------------------------------------------------")
    choice = input()
    if choice.lower() == 'x':
        os.system('cls')
        enterTown(hero)
    else:
        try:
            choice_index = int(choice) - 1 
            if 0 <= choice_index < len(hero.backpack):
                selected_item = hero.backpack[choice_index]
                if selected_item.itemType == "sword":
                    hero.equipWeapon(selected_item)
                os.system('cls')
                enterBackpack(hero)
            else:
                os.system('cls')
                print("Nieprawidłowy numer przedmiotu. Spróbuj ponownie.")
                enterBackpack(hero)
        except ValueError:
            os.system('cls')
            print("Nieprawidłowy wybór. Wprowadź numer przedmiotu lub 'X'.")
            enterBackpack(hero)