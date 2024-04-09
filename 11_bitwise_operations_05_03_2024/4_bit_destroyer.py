n = int(input())
p = int(input())

mask = ~(1 << p)

new_number = n & mask

print(new_number)
