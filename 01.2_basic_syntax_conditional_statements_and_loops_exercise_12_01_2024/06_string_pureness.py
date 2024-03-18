number = int(input())

for _ in range(number):
    text = input()
    for digit in range(len(text)):
        if text[digit] == "," or text[digit] == "." or text[digit] == "_":
            print(f"{text} is not pure!")
            break
    else:
        print(f"{text} is pure.")
