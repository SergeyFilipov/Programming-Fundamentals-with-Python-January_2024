string = input()
final_string = ""
last_added_character = ""

for character in string:
    if character != last_added_character:
        final_string += character
        last_added_character = character

print(final_string)
