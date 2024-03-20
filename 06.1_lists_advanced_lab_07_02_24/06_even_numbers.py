numbers = input().split(", ")

even_indices = [index for index, num in enumerate(numbers) if int(num) % 2 == 0]
print(even_indices)
