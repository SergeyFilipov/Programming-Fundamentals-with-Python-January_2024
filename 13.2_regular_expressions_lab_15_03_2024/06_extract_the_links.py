import re

patterno = r"(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)"
line = input()

while line:
    match = re.search(patterno, line)
    if match:
        print(match.group(1))

    line = input()
