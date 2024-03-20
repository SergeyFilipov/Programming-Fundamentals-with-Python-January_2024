message = input().split()

deciphered_massage = ''

for index in range(len(message)):
    word = message[index]
    deciphered_word = []
    num_in_word = []

    [num_in_word.append(i) for i in word if i.isdigit()]
    num = chr(int(''.join(num_in_word)))
    deciphered_word.insert(0, num)

    [deciphered_word.append(i) for i in word if not i.isdigit()]
    deciphered_word[1], deciphered_word[-1] = deciphered_word[-1], deciphered_word[1]

    if index == len(message) - 1:
        deciphered_massage += f"{''.join(deciphered_word)}"
    else:
        deciphered_massage += f"{''.join(deciphered_word)} "

print(deciphered_massage)
