resources = {}

while True:
    resource = input()

    if resource == "stop":
        break

    quantiy = int(input())
    if resource in resources:
        resources[resource] += quantiy
    else:
        resources[resource] = quantiy

for resource, quantiy in resources.items():
    print(f'{resource} -> {quantiy}')
