banned_list_word = input().split(", ")
text = input()

for banned_word in banned_list_word:
    text = text.replace(banned_word, "*" * len(banned_word))

print(text)
