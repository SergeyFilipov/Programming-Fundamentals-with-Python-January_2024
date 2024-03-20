text = input()

text_without_vowels = [char for char in text if char.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(text_without_vowels))
