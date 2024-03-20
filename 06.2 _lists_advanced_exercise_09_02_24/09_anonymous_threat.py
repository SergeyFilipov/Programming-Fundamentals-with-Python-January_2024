def valid_index(start, end):
    if start < 0:
        start = 0
    if end >= len(strings):
        end = len(strings) - 1
    return start, end


strings = input().split()
commands = input()
while commands != "3:1":
    command = commands.split()
    if command[0] == "merge":
        start_index, end_index = valid_index(int(command[1]), int(command[2]))
        strings[start_index:end_index + 1] = ["".join(strings[start_index:end_index + 1])]
    elif command[0] == "divide":
        index, partitions = int(command[1]), int(command[2])
        cut_part = len(strings[index]) // partitions
        text = strings.pop(index)
        counter = 1
        while True:
            if counter < partitions:
                strings.insert(index, text[:cut_part])
                text = (text[cut_part:])

            else:
                strings.insert(index, text)
                break
            index += 1
            counter += 1
    commands = input()
else:
    print(" ".join(strings))
