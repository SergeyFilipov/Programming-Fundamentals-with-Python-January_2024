# 1
def the_smallest_number(num1, num2, num3):
    min_num = min(num1, num2, num3)
    return min_num


num1 = int(input())
num2 = int(input())
num3 = int(input())
min_num = (the_smallest_number(num1, num2, num3))
print(min_num)


# 2
num1 = int(input())
num2 = int(input())
num3 = int(input())

print(min(num1, num2, num3))
