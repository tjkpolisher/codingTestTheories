import sys
input = sys.stdin.readline
book_sell = dict()

N = int(input())
for _ in range(N):
    book = input().rstrip()
    if book not in book_sell:
        book_sell[book] = 1
    else:
        book_sell[book] += 1

book_sell_list = list(book_sell.items())
book_sell_list.sort(key=lambda x: (-x[1], x[0]))
print(book_sell_list[0][0])