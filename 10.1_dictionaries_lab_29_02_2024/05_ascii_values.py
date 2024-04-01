input_characters = input()

ascii_dict = {char: ord(char) for char in input_characters.split(", ")}

print(ascii_dict)
