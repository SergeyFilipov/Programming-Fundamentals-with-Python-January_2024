def calculator():
    operation = input()
    num1 = int(input())
    num2 = int(input())

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = int(num1 / num2)

    return result


print(calculator())
