lessons = input().split(", ")
command = input()

while not command == "course start":
    action, *args = command.split(":")
    lesson = args[0]
    if action == "Add":
        if lesson not in lessons:
            lessons.append(lesson)
    elif action == "Insert":
        index = int(args[1])
        if lesson not in lessons:
            lessons.insert(index, lesson)
    elif action == "Remove":
        if lesson in lessons:
            lessons.remove(lesson)
            if f"{lesson}-Exercise" in lessons:
                lessons.remove(f"{lesson}-Exercise")
    elif action == "Swap":
        lesson_1, lesson_2 = args
        if lesson_1 in lessons and lesson_2 in lessons:
            index_1, index_2 = lessons.index(lesson_1), lessons.index(lesson_2)
            lessons[index_1], lessons[index_2] = lessons[index_2], lessons[index_1]
            if f"{lesson_1}-Exercise" in lessons and f"{lesson_2}-Exercise" in lessons:
                index_ex_1 = lessons.index(f"{lesson_1}-Exercise")
                index_ex_2 = lessons.index(f"{lesson_2}-Exercise")
                lessons[index_ex_1], lessons[index_ex_2] = lessons[index_ex_2], lessons[index_ex_1]
    elif action == "Exercise":
        if lesson in lessons:
            exercise = f"{lesson}-Exercise"
            index = lessons.index(lesson) + 1
            if exercise not in lessons:
                lessons.insert(index, exercise)
    command = input()

for i, lesson in enumerate(lessons, start=1):
    print(f"{i}.{lesson}")
