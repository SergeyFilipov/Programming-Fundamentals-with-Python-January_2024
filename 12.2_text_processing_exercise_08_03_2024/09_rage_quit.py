text = input()
rage_message = ""
repetitions = ""
current_symbol = ""

for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index].upper()

    else:
        for next_symbol in range(index, len(text)):
            if not text[next_symbol].isdigit():
                break
            repetitions += text[next_symbol]
        rage_message += current_symbol * int(repetitions)
        repetitions = ""
        current_symbol = ""

print(f"Unique symbols used: {len(set(rage_message))}\n{rage_message}")
