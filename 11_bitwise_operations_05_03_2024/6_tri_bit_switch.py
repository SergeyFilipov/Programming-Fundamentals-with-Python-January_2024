def invert_bits(number, p):
    mask = 7 << p
    result = number ^ mask
    return result


number = int(input())
p = int(input())

print(invert_bits(number, p))
