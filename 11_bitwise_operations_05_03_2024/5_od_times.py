numbers = list(map(int, input().split()))

result = 0

for num in numbers:
    result ^= num

print(result)
