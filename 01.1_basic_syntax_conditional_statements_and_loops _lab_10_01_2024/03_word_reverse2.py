word = input()

# 1
for _ in range(len(word) - 1, - 1, - 1):
    print(word[_], end="")

# 2
for _ in word[::-1]:
    print(_, end="")
