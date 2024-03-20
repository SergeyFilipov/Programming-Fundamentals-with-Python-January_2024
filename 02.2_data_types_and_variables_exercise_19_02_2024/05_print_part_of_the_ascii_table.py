start_index = int(input())
finish_index = int(input())

for index_in_ascii in range(start_index, finish_index + 1):
    print(chr(index_in_ascii), end=" ")
