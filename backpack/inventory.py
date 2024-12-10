import os


def enterBackpack(hero):
    from town.town import enterTown
    print("--------------------------------------------------")
    print("----------------------\033[92mPlecak\033[0m----------------------")
    print("--------------------------------------------------")
    for index, item in enumerate(hero.backpack, start=1):
        match item.itemType:
            case "weapon": 
                if item.isEquipped == False:
                    print(f"| {index}. \033[94m{item.name}\033[0m | Obrażenia: \033[91m{item.minAttack}\033[0m - \033[91m{item.maxAttack}\033[0m ")
                else:
                    print(f"| {index}. \033[94m{item.name}\033[0m | Obrażenia: \033[91m{item.minAttack}\033[0m - \033[91m{item.maxAttack}\033[0m | \033[36mZałożono\033[0m")
            case "helmet": 
                if item.isEquipped == False:
                    print(f"| {index}. \033[96m{item.name}\033[0m | Obrona: \033[36m{item.defense}\033[0m ")
                else:
                    print(f"| {index}. \033[96m{item.name}\033[0m | Obrona: \033[36m{item.defense}\033[0m | \033[36mZałożono\033[0m")
            case "chest": 
                if item.isEquipped == False:
                    print(f"| {index}. \033[95m{item.name}\033[0m | Obrona: \033[36m{item.defense}\033[0m ")
                else:
                    print(f"| {index}. \033[95m{item.name}\033[0m | Obrona: \033[36m{item.defense}\033[0m | \033[36mZałożono\033[0m")
            case "leggings": 
                if item.isEquipped == False:
                    print(f"| {index}. \033[93m{item.name}\033[0m | Obrona: \033[36m{item.defense}\033[0m ")
                else:
                    print(f"| {index}. \033[93m{item.name}\033[0m | Obrona: \033[36m{item.defense}\033[0m | \033[36mZałożono\033[0m")
            case "other":
                    print(f"| {index}. \033[35m{item.name}\033[0m | Ilość: \033[97m{item.amount}\033[0m ")
    print("--------------------------------------------------")
    print("| \033[4m\033[37mWybierz numer przedmiotu\033[0m ------------------------------")
    print("| \033[4m\033[32mX. Wróć\033[0m ----------------------------------------")
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
                        equipmentChoice(selected_item, hero, hero.weapon, hero.takeOffWeapon, hero.replaceWeapon, hero.equipWeapon, hero.deleteWeapon)
                    case "helmet":
                        equipmentChoice(selected_item, hero, hero.helmet, hero.takeOffHelmet, hero.replaceHelmet, hero.equipHelmet, hero.deleteHelmet)
                    case "chest":
                        equipmentChoice(selected_item, hero, hero.chest, hero.takeOffChest, hero.replaceChest, hero.equipChest, hero.deleteChest)
                    case "leggings":
                        equipmentChoice(selected_item, hero, hero.leggings, hero.takeOffLeggings, hero.replaceLeggings, hero.equipLeggings, hero.deleteLeggings)
                    case "other":
                        otherEquipmentChoice(selected_item, hero, hero.deleteOtherItem)
                os.system('cls')
                enterBackpack(hero)
            else:
                os.system('cls')
                print("\033[31mNieprawidłowy numer przedmiotu. Spróbuj ponownie\033[0m")
                enterBackpack(hero)
        except ValueError:
            os.system('cls')
            print("\033[31mNieprawidłowy wybór. Wprowadź numer przedmiotu lub 'X'\033[0m")
            enterBackpack(hero)

def equipmentChoice(selected_item, hero, heroTypeOfEquipment, takeOff, replace, equip, delete):
    os.system("cls")
    print(f"Co chcesz zrobić z \033[1m{selected_item.name} \033[0m?")
    print("------------------------------------------------------")                   
    if selected_item.isEquipped:
        print("| \033[4m\033[32m1. Zdejmij z eq\033[0m ------------------------------------")
    elif not selected_item.isEquipped and heroTypeOfEquipment == None:
        print("| \033[4m\033[32m1. Załóż\033[0m -------------------------------------------")
    else:
        print("| \033[4m\033[32m1. Podmień \033[0m ----------------------------------------")
    print("| \033[4m\033[31m2. Wyrzuć\033[0m ------------------------------------------")
    print("| \033[4m\033[33m3. Wróć\033[0m --------------------------------------------")
    print("------------------------------------------------------")
    itemChoice = input()
    if selected_item.isEquipped and itemChoice == "1":
        takeOff(selected_item)
        hero.updateDefense()
        os.system('cls')
        enterBackpack(hero)
    elif not selected_item.isEquipped and heroTypeOfEquipment is not None and itemChoice == "1":
        replace(selected_item, heroTypeOfEquipment)
        hero.updateDefense()
        os.system('cls')
        enterBackpack(hero)
    elif not selected_item.isEquipped and itemChoice == "1":
        equip(selected_item)
        hero.updateDefense()
        os.system('cls')
        enterBackpack(hero)
    elif itemChoice == "2":
        delete(selected_item)
        hero.updateDefense()
        os.system('cls')
        enterBackpack(hero)
    elif itemChoice == "3":
        os.system('cls')
        enterBackpack(hero)
    else:
        os.system('cls')
        print("\033[31mNieprawidłowy wybór. Spróbuj ponownie\033[0m")
        enterBackpack(hero)

def otherEquipmentChoice(selected_item, hero, delete):
    os.system("cls")
    print(f"Co chcesz zrobić z \033[1m{selected_item.name} \033[0m?")
    print("------------------------------------------------------")
    print("| \033[4m\033[31m1. Wyrzuć\033[0m ------------------------------------------")
    print("| \033[4m\033[33m2. Wróć\033[0m --------------------------------------------")
    print("------------------------------------------------------")
    itemChoice = input()
    if itemChoice == "1":
        delete(selected_item)
        os.system('cls')
        enterBackpack(hero)
    elif itemChoice == "2":
        os.system('cls')
        enterBackpack(hero)
    else:
        os.system('cls')
        print("\033[31mNieprawidłowy wybór. Spróbuj ponownie\033[0m")
        enterBackpack(hero)