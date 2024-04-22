file_path = input().split("\\")
file_name_and_extension = file_path[-1].split(".")

print(f"File name: {file_name_and_extension[0]}")
print(f"File extension: {file_name_and_extension[1]}")
