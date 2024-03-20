import math

count_of_people = int(input())
capacity_elevator = int(input())

courses = count_of_people / capacity_elevator
print(math.ceil(courses))
