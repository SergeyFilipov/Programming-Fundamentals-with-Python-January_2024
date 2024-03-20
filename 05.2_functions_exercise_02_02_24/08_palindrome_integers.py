def palindrome_function(list):
    result = ""

    for number in list:
        if str(number) == str(number)[::-1]:
            result += "True\n"
        else:
            result += "False\n"

    return result


list_of_palindromes = list(map(int, input().split(", ")))
print(palindrome_function(list_of_palindromes))
