from collections import deque
N = int(input())
card_deck = deque(range(1, N + 1))
while len(card_deck) > 1:
    print(card_deck[0], end=' ')
    card_deck.popleft()
    next_card = card_deck.popleft()
    card_deck.append(next_card)
print(card_deck[0], end=' ')