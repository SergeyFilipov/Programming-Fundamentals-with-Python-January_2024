count_of_rooms = int(input())
total_free_chairs = 0
for number_of_room in range(1, count_of_rooms + 1):
    free_chairs_in_current_room, visitors = input().split()
    difference = len(free_chairs_in_current_room) - int(visitors)
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {number_of_room}")
    total_free_chairs += difference
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")
