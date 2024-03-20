def calculate_rectangle_area(length, width):
    area = length * width
    return area


length = int(input())
width = int(input())
area = calculate_rectangle_area(length, width)
print(area)
