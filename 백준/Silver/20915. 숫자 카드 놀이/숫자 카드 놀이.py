T = int(input())
for _ in range(T):
    cards = input().replace('6', '9')
    cards = sorted(list(cards), reverse=True)

    zeros = cards.count('0')
    for i in range(zeros):
        cards.pop()
    if not cards:
        print(0)
        continue

    num1 = int(cards[0])
    num2 = 0
    for i in range(1, len(cards)):
        if num1 > num2:
            num2 = num2 * 10 + int(cards[i])
        else:
            num1 = num1 * 10 + int(cards[i])
    for i in range(zeros):
        num1 *= 10
    print(num1 * num2)