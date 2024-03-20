distance = [int(number) for number in input().split()]
sum_of_removed_elements = 0
while distance:  # while len(distance) > 0
    index = int(input())
    removed_element = 0
    if index < 0:
        removed_element = distance[0]
        distance[0] = distance[-1]
    elif index >= len(distance):
        removed_element = distance[-1]
        distance[-1] = distance[0]
    else:  # Index is valid
        removed_element = distance.pop(index)
    sum_of_removed_elements += removed_element
    for manipulating_index in range(len(distance)):
        if distance[manipulating_index] <= removed_element:
            distance[manipulating_index] += removed_element
        else:  # distance_list[manipulating_index] > removed_element
            distance[manipulating_index] -= removed_element
print(sum_of_removed_elements)
