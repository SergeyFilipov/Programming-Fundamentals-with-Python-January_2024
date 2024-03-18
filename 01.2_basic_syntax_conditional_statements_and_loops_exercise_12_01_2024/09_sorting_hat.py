while True:
    current_command = input()
    if current_command == "Welcome!":
        print(f"Welcome to Hogwarts.")
        break
    elif current_command == "Voldemort":
        print(f"You must not speak of that name!")
        break
    elif len(current_command) < 5:
        print(f"{current_command} goes to Gryffindor.")
    elif len(current_command) == 5:
        print(f"{current_command} goes to Slytherin.")
    elif len(current_command) == 6:
        print(f"{current_command} goes to Ravenclaw.")
    elif len(current_command) > 6:
        print(f"{current_command} goes to Hufflepuff.")
