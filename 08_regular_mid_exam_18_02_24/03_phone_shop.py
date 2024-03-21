phone_list = input().split(", ")
command = input().split(" - ")

while command[0] != "End":
    action = command[0]
    item = command[1]

    if action == "Add":
        if item not in phone_list:
            phone_list.append(item)

    elif action == "Remove":
        if item in phone_list:
            phone_list.remove(item)

    elif action == "Bonus phone":
        old_phone, new_phone = item.split(":")

        if old_phone in phone_list:
            old_phone_index = phone_list.index(old_phone)
            phone_list.insert(old_phone_index + 1, new_phone)

    elif action == "Last":
        if item in phone_list:
            phone_list.remove(item)
            phone_list.append(item)

    command = input().split(" - ")

print(", ".join(phone_list))
