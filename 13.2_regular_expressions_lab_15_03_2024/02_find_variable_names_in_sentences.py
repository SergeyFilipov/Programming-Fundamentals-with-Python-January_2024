import re

sentence = input()
pattern = r"\b_([a-zA-Z0-9]+)\b"
variables = re.findall(pattern, sentence)
print(",".join(variables))
