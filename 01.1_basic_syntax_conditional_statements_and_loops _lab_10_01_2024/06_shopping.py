budget = int(input())
command = int(input())

while command != "End":
    product_sum = int(command)
    budget = budget - product_sum
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")
