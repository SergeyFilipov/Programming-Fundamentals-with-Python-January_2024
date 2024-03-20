# 1
def sum_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(result, num3):
    return result - num3


def add_and_subtract(num1, num2, num3):
    result = sum_numbers(num1, num2)
    return subtract_numbers(result, num3)


num1 = int(input())
num2 = int(input())
num3 = int(input())
subtract = add_and_subtract(num1, num2, num3)
print(subtract)


# 2
def add_and_subtract(num1, num2, num3):
    result = (num1 + num2) - num3
    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())
subtract = add_and_subtract(num1, num2, num3)
print(subtract)
