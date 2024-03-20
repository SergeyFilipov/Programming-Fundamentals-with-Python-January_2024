# 1
string_text = input().split()

words = [word for word in string_text if len(word) % 2 == 0]
print("\n".join(words))


# 2
string_text = input().split()

for word in string_text:
    if len(word) % 2 == 0:
        print(word)
