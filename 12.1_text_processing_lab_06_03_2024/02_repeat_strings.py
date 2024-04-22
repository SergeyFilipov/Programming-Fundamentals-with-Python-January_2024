words = input().split()
result = [text * len(text) for text in words]
print(''.join(result))
