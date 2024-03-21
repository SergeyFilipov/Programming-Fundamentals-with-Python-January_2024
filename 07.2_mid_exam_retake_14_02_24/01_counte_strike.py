energy = int(input())

still_have_energy = True
won_battles = 0
command = input()

while command != "End of battle":
    currant_distance = int(command)

    if energy - currant_distance < 0:
        still_have_energy = False
        break
    energy -= currant_distance
    won_battles += 1

    if won_battles % 3 == 0:
        energy += won_battles

    command = input()

if still_have_energy:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
