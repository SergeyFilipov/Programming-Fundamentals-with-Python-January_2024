mixed_string = input()
numbers = ""
letters = ""
others = ""

for char in mixed_string:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        others += char

print(f"{numbers}\n{letters}\n{others}")
