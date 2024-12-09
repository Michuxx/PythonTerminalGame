import os

def enterBackpack(hero):
    from town.town import enterTown
    print("--------------------------------------------------")
    print("----------------------Plecak----------------------")
    print("--------------------------------------------------")
    for index, item in enumerate(hero.backpack, start=1):
        if item.itemType == "weapon":
            if item.isEquipped == False:
                print(f"| {index}. {item.name} | Obrażenia: {item.minAttack} - {item.maxAttack} ")
            else:
                print(f"| {index}. {item.name} | Obrażenia: {item.minAttack} - {item.maxAttack} | Założono")
        if item.itemType =="helmet":
            if item.isEquipped == False:
                print(f"| {index}. {item.name} | Obrona: {item.defense} ")
            else:
                print(f"| {index}. {item.name} | Obrona: {item.defense} | Założono")
        if item.itemType =="chest":
            if item.isEquipped == False:
                print(f"| {index}. {item.name} | Obrona: {item.defense} ")
            else:
                print(f"| {index}. {item.name} | Obrona: {item.defense} | Założono")
        if item.itemType =="leggings":
            if item.isEquipped == False:
                print(f"| {index}. {item.name} | Obrona: {item.defense} ")
            else:
                print(f"| {index}. {item.name} | Obrona: {item.defense} | Założono")
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
                match selected_item.itemType:
                    case "weapon":
                        equipmentChoice(selected_item, hero, hero.weapon)
                    case "helmet":
                        equipmentChoice(selected_item, hero, hero.helmet)
                    case "chest":
                        equipmentChoice(selected_item, hero, hero.chest)
                    case "leggings":
                        equipmentChoice(selected_item, hero, hero.leggings)
                os.system('cls')
                enterBackpack(hero)
            else:
                os.system('cls')
                print("Nieprawidłowy numer przedmiotu. Spróbuj ponownie")
                enterBackpack(hero)
        except ValueError:
            os.system('cls')
            print("Nieprawidłowy wybór. Wprowadź numer przedmiotu lub 'X'.")
            enterBackpack(hero)

def equipmentChoice(selected_item, hero, heroTypeOfEquipment):
    os.system("cls")
    print(f"Co chcesz zrobić z {selected_item.name} ?")
    print("--------------------------------------------------")                   
    if selected_item.isEquipped:
        print("| 1. Zdejmij z eq ----------------------------")
    elif not selected_item.isEquipped and heroTypeOfEquipment == None:
        print("| 1. Załóż -----------------------------------")
    else:
        print("| 1. Podmień ---------------------------------")
    print("| 2. Wyrzuć ----------------------------------")
    print("| 3. Wróć ----------------------------------")
    print("--------------------------------------------------")
    itemChoice = input()
    if selected_item.isEquipped and itemChoice == "1":
        hero.takeOffWeapon(selected_item)
        os.system('cls')
        enterBackpack(hero)
    elif not selected_item.isEquipped and heroTypeOfEquipment is not None and itemChoice == "1":
        hero.replaceWeapon(selected_item, heroTypeOfEquipment)
        os.system('cls')
        enterBackpack(hero)
    elif not selected_item.isEquipped and itemChoice == "1":
        hero.equipWeapon(selected_item)
        os.system('cls')
        enterBackpack(hero)
    elif itemChoice == "2":
        hero.deleteWeapon(selected_item)
        os.system('cls')
        enterBackpack(hero)
    elif itemChoice == "3":
        os.system('cls')
        enterBackpack(hero)
    else:
        os.system('cls')
        print("Nieprawidłowy wybór. Spróbuj ponownie")
        enterBackpack(hero)