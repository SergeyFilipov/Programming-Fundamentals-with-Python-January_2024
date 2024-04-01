words = input().lower().split()

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

for word, count in word_counts.items():
    if count % 2 != 0:
        print(word.lower(), end=" ")
