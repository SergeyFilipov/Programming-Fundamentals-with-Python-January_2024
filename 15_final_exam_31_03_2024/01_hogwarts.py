spell = input()

while True:
    command = input().split()

    if command[0] == "Abracadabra":
        break

    if command[0] == "Abjuration":
        spell = spell.upper()
        print(spell)

    elif command[0] == "Necromancy":
        spell = spell.lower()
        print(spell)

    elif command[0] == "Illusion":
        index = int(command[1])
        letter = command[2]

        if index < 0 or index >= len(spell):
            print("The spell was too weak.")
        else:
            spell = spell[:index] + letter + spell[index + 1:]
            print("Done!")

    elif command[0] == "Divination":
        first_substring = command[1]
        second_substring = command[2]

        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)

    elif command[0] == "Alteration":
        substring = command[1]

        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)

    else:
        print("The spell did not work!")
