def pick_up_card(hand, card):
    hand.append(card)
    i = len(hand) - 2
    while i >= 0 and hand[i] > card:
        hand[i + 1] = hand[i]
        i -= 1
    hand[i + 1] = card
    return hand

hand = []
for c in [7, 2, 9, 4, 1]:
    hand = pick_up_card(hand, c)
print(hand)