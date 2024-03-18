number_of_messages = int(input())
messages = ""
for _ in range(number_of_messages):
    number = int(input())
    if number == 88:
        messages = "Hello"
    elif number == 86:
        messages = "How are you?"
    elif number < 88 and number != 86 and number != 88:
        messages = "GREAT!"
    elif 88 < number:
        messages = "Bye."
    print(f"{messages}")
