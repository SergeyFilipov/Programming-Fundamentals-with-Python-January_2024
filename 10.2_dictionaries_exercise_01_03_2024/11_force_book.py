def manage_force_profiles(commands):
    force_sides = {}

    for command in commands:

        if " | " in command:

            force_side, force_user = command.split(" | ")

            if force_side not in force_sides:
                force_sides[force_side] = []

            if force_user not in force_sides.values():

                for side in force_sides:

                    if force_user in force_sides[side]:
                        break
                else:

                    force_sides[force_side].append(force_user)


        elif " -> " in command:

            force_user, force_side = command.split(" -> ")

            for side, users in force_sides.items():

                if force_user in users:
                    users.remove(force_user)

                    break

            force_sides.setdefault(force_side, []).append(force_user)

            print(f"{force_user} joins the {force_side} side!")

    return force_sides


def print_force_sides(force_sides):
    for side, users in force_sides.items():
        if users:

            print(f"Side: {side}, Members: {len(users)}")
            for user in users:
                print(f"! {user}")


def main():
    commands = []

    while True:
        command = input()
        if command == "Lumpawaroo":
            break

        commands.append(command)

    force_sides = manage_force_profiles(commands)

    print_force_sides(force_sides)


if __name__ == "__main__":
    main()
