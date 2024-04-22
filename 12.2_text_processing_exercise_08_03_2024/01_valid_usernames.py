def length_is_valid(name):
    if 3 <= len(name) < 16:
        return True
    return False


def charackters_are_valid(name):
    for character in name:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def no_redundant_symbols(name):
    if " " in name:
        return False
    return True


usernames = input().split(", ")

for username in usernames:
    if length_is_valid(username) and charackters_are_valid(username) and no_redundant_symbols(username):
        print(username)
