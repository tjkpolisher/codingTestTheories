import sys
import heapq
input = sys.stdin.readline

N = int(input())
cards = []
for _ in range(N):
    data = int(input())
    heapq.heappush(cards, data)

result = 0

while len(cards) > 1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    new_card = card1 + card2

    result += new_card
    heapq.heappush(cards, new_card)

print(result)