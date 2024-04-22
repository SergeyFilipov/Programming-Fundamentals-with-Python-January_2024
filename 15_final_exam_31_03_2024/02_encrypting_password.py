import re

n = int(input())

for _ in range(n):
    password = input()

    pattern_valid = r'^(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|(.+)<\1$'

    match = re.match(pattern_valid, password)

    if match:
        encrypted_password = match.group(2) + match.group(3) + match.group(4) + match.group(5)
        print(f"Password: {encrypted_password}")
    else:
        print("Try another password!")
