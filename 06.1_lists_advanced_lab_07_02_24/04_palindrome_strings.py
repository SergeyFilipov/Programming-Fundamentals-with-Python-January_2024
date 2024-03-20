words = input().split()
palindrome_word = input()
palindrome_list = []

for word in words:
    if str(word) == str(word)[::-1]:
        palindrome_list.append(word)
    else:
        continue

print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(palindrome_word)} times")
