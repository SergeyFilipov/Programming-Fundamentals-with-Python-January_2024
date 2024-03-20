def calculate_rectangle_properties(length, width):
    area = length * width
    diagonals = (length ** 2 + width ** 2) ** 0.5
    perimeter = 2 * (length + width)

    return area, diagonals, perimeter


area, diagonals, perimeter = calculate_rectangle_properties(length=10, width=3)
print("Area: ", area)
print(f"Diagonals: {diagonals:.2f}")
print("Perimeter: ", perimeter)
