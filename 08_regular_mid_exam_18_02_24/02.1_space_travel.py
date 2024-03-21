route = input().split("||")
start_fuel = int(input())
start_ammunition = int(input())

mission_status = "Ongoing"
reached_titan = False

for action in route:
    parts = action.split()
    command = parts[0]

    if len(parts) > 1:
        value = int(parts[1])

    if command == "Travel":
        if start_fuel >= value:
            print(f"The spaceship travelled {value} light-years.")
            start_fuel -= value
        else:
            print("Mission failed.")
            mission_status = "Failed"
            break
    elif command == "Enemy":
        if start_ammunition >= value:
            print(f"An enemy with {value} armour is defeated.")
            start_ammunition -= value
        elif start_fuel >= value * 2:
            print(f"An enemy with {value} armour is outmaneuvered.")
            start_fuel -= value * 2
        else:
            print("Mission failed.")
            mission_status = "Failed"
            break
    elif command == "Repair":
        if len(parts) > 1:
            added_ammunition = value
            added_fuel = value
            added_ammunition *= 2
            print(f"Ammunitions added: {added_ammunition}.")
            print(f"Fuel added: {added_fuel}.")
            start_ammunition += added_ammunition
            start_fuel += added_fuel
        else:
            print("Mission failed.")
            mission_status = "Failed"
            break

    if command == "Titan":
        reached_titan = True
        print("You have reached Titan, all passengers are safe.")
        break
