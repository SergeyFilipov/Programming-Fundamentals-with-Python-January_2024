def travel(distance, fuel):
    """Simulate travel action."""
    if fuel >= distance:
        print(f"The spaceship travelled {distance} light-years.")
        return fuel - distance
    else:
        print("Mission failed.")
        return None


def enemy(encounter, ammunition, fuel):
    """Simulate encounter with enemy."""
    if ammunition >= encounter:
        print(f"An enemy with {encounter} armour is defeated.")
        return ammunition - encounter, fuel
    elif fuel >= encounter * 2:
        print(f"An enemy with {encounter} armour is outmaneuvered.")
        return ammunition, fuel - encounter * 2
    else:
        print("Mission failed.")
        return None, None


def repair(added_ammunition, added_fuel, ammunition, fuel):
    """Simulate repair action."""
    added_ammunition *= 2
    print(f"Ammunitions added: {added_ammunition}.")
    print(f"Fuel added: {added_fuel}.")
    return ammunition + added_ammunition, fuel + added_fuel


def mission(route, start_fuel, start_ammunition):
    """Simulate the entire mission."""
    mission_status = "Ongoing"
    reached_titan = False

    for action in route:
        parts = action.split()
        command = parts[0]

        if len(parts) > 1:
            value = int(parts[1])

        if command == "Travel":
            start_fuel = travel(value, start_fuel)
            if start_fuel is None:
                mission_status = "Failed"
                break

        elif command == "Enemy":
            start_ammunition, start_fuel = enemy(value, start_ammunition, start_fuel)
            if start_ammunition is None:
                mission_status = "Failed"
                break

        elif command == "Repair":
            if len(parts) > 1:
                start_ammunition, start_fuel = repair(value, value, start_ammunition, start_fuel)
            else:
                print("Mission failed.")
                mission_status = "Failed"
                break

        elif command == "Titan":
            reached_titan = True
            print("You have reached Titan, all passengers are safe.")
            break

    if reached_titan:
        return "Success"
    elif mission_status == "Failed":
        return "Failed"
    else:
        return "Ongoing"


route = input().split("||")
start_fuel = int(input())
start_ammunition = int(input())

result = mission(route, start_fuel, start_ammunition)
