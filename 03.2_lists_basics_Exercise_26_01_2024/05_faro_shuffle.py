cards = input().split()
count_shuffles = int(input())

for shuffles in range(count_shuffles):
    middle_deck = len(cards) // 2
    left_part = cards[0:middle_deck]
    right_part = cards[middle_deck:]
    deck_after_shuffling = []
    for card_index in range(len(left_part)):
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append(right_part[card_index])
    cards = deck_after_shuffling

print(cards)
