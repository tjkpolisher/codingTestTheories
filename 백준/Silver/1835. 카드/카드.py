from collections import deque

N = int(input())
deck = deque([N])
num = N

while len(deck) < N:
    num -= 1
    deck.appendleft(num)
    for _ in range(num):
        p = deck.pop()
        deck.appendleft(p)

print(*deck)