def check_farm_progress(dictionary):
    if dictionary["shards"] >= 250:
        dictionary["shards"] -= 250
        print(f"Shadowmourne obtained!")
        return True
    elif dictionary["fragments"] >= 250:
        dictionary["fragments"] -= 250
        print(f"Valanyr obtained!")
        return True
    elif dictionary["motes"] >= 250:
        dictionary["motes"] -= 250
        print(f"Dragonwrath obtained!")
        return True
    else:
        return False


def print_inventory(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")


def main():
    inventory = {'shards': 0, 'fragments': 0, 'motes': 0}
    itemFound = False
    while True:
        if itemFound:
            break
        inputList = input().split()
        for i in range(0, len(inputList), 2):
            if itemFound:
                break
            amount = inputList[i]
            material = inputList[i + 1]
            material = material.lower()
            if material in inventory:
                inventory[material] += int(amount)
            else:
                inventory[material] = int(amount)
            if check_farm_progress(inventory):
                itemFound = True
                break
    print_inventory(inventory)


if __name__ == "__main__":
    main()
