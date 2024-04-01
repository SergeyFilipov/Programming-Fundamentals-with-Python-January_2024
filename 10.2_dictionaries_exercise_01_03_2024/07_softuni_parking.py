def validate_parking(commands):
    parking_lot = {}

    for command in commands:
        action, *args = command.split()

        if action == "register":
            username, license_plate = args[0], args[1]
            if username in parking_lot:
                print(f"ERROR: already registered with plate number {parking_lot[username]}")
            else:
                parking_lot[username] = license_plate
                print(f"{username} registered {license_plate} successfully")
        elif action == "unregister":
            username = args[0]
            if username not in parking_lot:
                print(f"ERROR: user {username} not found")
            else:
                del parking_lot[username]
                print(f"{username} unregistered successfully")

    for username, license_plate in parking_lot.items():
        print(f"{username} => {license_plate}")


def main():
    n = int(input())
    commands = [input() for _ in range(n)]
    validate_parking(commands)


if __name__ == "__main__":
    main()
