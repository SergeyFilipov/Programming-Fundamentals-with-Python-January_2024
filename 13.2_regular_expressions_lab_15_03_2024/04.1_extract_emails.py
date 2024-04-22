import re


def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    emails = re.findall(pattern, text)

    return emails


text = input()

for email in extract_emails(text):
    print(email)
