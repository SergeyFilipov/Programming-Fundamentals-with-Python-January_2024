number_of_coffees = 0
command = input()

while command != "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        number_of_coffees += 1
        command = input()
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        number_of_coffees += 2
        command = input()
    else:
        command = input()
if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)
