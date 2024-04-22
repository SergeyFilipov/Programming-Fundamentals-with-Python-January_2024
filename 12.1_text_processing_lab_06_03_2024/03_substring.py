key_word = input()
text = input()

while key_word in text:
    text = text.replace(key_word, "")
print(text)
