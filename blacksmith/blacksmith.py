import os

def enterBlacksmith(hero):
    from town.town import enterTown
    print("--------------------------------------------------")
    print("----------------------\033[33mKowal\033[0m----------------------")
    print("--------------------------------------------------")
    for index, item in enumerate(backpackWithoutOtherItems(hero), start=1):
        match item.itemType:
            case "weapon": 
                if item.isEquipped == False:
                    print(f"| {index}. \033[94m{item.name}\033[0m +{item.upgrade} | Obrażenia: \033[91m{item.minAttack}\033[0m - \033[91m{item.maxAttack}\033[0m ")
                else:
                    print(f"| {index}. \033[94m{item.name}\033[0m +{item.upgrade} | Obrażenia: \033[91m{item.minAttack}\033[0m - \033[91m{item.maxAttack}\033[0m | \033[36mZałożono\033[0m")
            case "helmet": 
                if item.isEquipped == False:
                    print(f"| {index}. \033[96m{item.name}\033[0m +{item.upgrade} | Obrona: \033[36m{item.defense}\033[0m ")
                else:
                    print(f"| {index}. \033[96m{item.name}\033[0m +{item.upgrade} | Obrona: \033[36m{item.defense}\033[0m | \033[36mZałożono\033[0m")
            case "chest": 
                if item.isEquipped == False:
                    print(f"| {index}. \033[95m{item.name}\033[0m +{item.upgrade} | Obrona: \033[36m{item.defense}\033[0m ")
                else:
                    print(f"| {index}. \033[95m{item.name}\033[0m +{item.upgrade} | Obrona: \033[36m{item.defense}\033[0m | \033[36mZałożono\033[0m")
            case "leggings": 
                if item.isEquipped == False:
                    print(f"| {index}. \033[93m{item.name}\033[0m +{item.upgrade} | Obrona: \033[36m{item.defense}\033[0m ")
                else:
                    print(f"| {index}. \033[93m{item.name}\033[0m +{item.upgrade} | Obrona: \033[36m{item.defense}\033[0m | \033[36mZałożono\033[0m")
    print("--------------------------------------------------")
    print("| \033[4m\033[32mWybierz numer przedmiotu, który chcesz ulepszyć\033[0m")
    print("| \033[4m\033[33mX. Wróć\033[0m ----------------------------------------")
    print("--------------------------------------------------")
    choice = input()
    if choice.lower() == 'x':
        os.system('cls')
        enterTown(hero)
    else:
        try:
            choice_index = int(choice) - 1 
            if 0 <= choice_index < len(backpackWithoutOtherItems(hero)):
                selected_item = hero.backpack[choice_index]
                upgradeItem(selected_item, hero)
            else:
                os.system('cls')
                print("\033[31mNieprawidłowy numer przedmiotu. Spróbuj ponownie\033[0m")
                enterBlacksmith(hero)
        except ValueError:
            os.system('cls')
            print("\033[31mNieprawidłowy wybór. Wprowadź numer przedmiotu lub 'X'\033[0m")
            enterBlacksmith(hero)

def upgradeItem(selected_item, hero):
    os.system("cls")
    print(f"Czy na pewno chcesz ulepszyć \033[1m{selected_item.name}\033[0m z \033[1m+{selected_item.upgrade}\033[0m na \033[1m+{selected_item.upgrade + 1}\033[0m ?\nBędzie to kosztować \033[1m{selected_item.materials.amount}\033[0m \033[1m{selected_item.materials.name}\033[0m")
    print("------------------------------------------------------")
    print("| \033[4m\033[96m1. Ulepsz\033[0m ------------------------------------------")
    print("| \033[4m\033[33m2. Wróć\033[0m --------------------------------------------")
    print("------------------------------------------------------")
    upgradeChoice = input()
    match upgradeChoice:
        case "1":
            if isUpgradeably(selected_item, hero):
                match selected_item.itemType:
                    case "weapon":
                        selected_item.upgradeWeapon()
                    case "helmet":
                        selected_item.upgradeHelmet()
                    case "leggings":
                        selected_item.upgradeLeggings()
                    case "chest":
                        selected_item.upgradeChest()
                selected_item.updateStatistics()
                hero.updateOtherItem(selected_item)
                hero.updateDefense()
                os.system("cls")
                print("\033[92mUlepszono przedmiot !\033[0m")
                enterBlacksmith(hero)
            else:
                os.system("cls")
                print("\033[31mBrakuje ci materiałów do ulepszenia tego przedmiotu !\033[0m")
                enterBlacksmith(hero)
        case "2":
            os.system('cls')
            enterBlacksmith(hero)
        case _:
            os.system('cls')
            print("\033[31mNieprawidłowa opcja... Wybierz jeszcze raz\033[0m")
            enterBlacksmith(hero)

def isUpgradeably(selected_item, hero):
    for i in range(len(hero.backpack)):
        if selected_item.materials.name == hero.backpack[i].name:
            if selected_item.materials.amount <= hero.backpack[i].amount:
                return True
    return False

def backpackWithoutOtherItems(hero):
    newBackpack= []
    for i in range(len(hero.backpack)):
        if hero.backpack[i].itemType != "other":
            newBackpack.append(hero.backpack[i])
    return newBackpack