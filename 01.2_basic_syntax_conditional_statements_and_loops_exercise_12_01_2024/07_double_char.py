command = input()
while command != "End":
    if command == "SoftUni":
        command = input()
    new_command = ""
    for symbol in command:
        new_command += symbol * 2
    print(new_command)
    command = input()
