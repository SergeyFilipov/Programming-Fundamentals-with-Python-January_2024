## 1
def coun_letters(current_text):
    chars_dict = {}

    for word in current_text:
        for letter in word:
            if letter not in chars_dict:
                chars_dict[letter] = 1
            else:
                chars_dict[letter] += 1
    return chars_dict


string = input().split()
char_dict = coun_letters(string)

for key, vaulue in char_dict.items():
    print(f"{key} -> {vaulue}")


## 2
def count_characters(string):
    char_count = {}

    for char in string:
        if char != " ":
            char_count[char] = char_count.get(char, 0) + 1

    for char, count in char_count.items():
        print(f"{char} -> {count}")


input_string = input()
count_characters(input_string)
