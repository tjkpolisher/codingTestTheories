import sys
from collections import Counter
input = sys.stdin.readline


def is_true(numbers):
    if numbers[0] + 1 == numbers[1] and numbers[1] + 1 == numbers[2]:
        return True
    return False


def rule1(cards):
    # 알파벳이 같으면서 숫자가 연속되는 세 장이 존재.
    alphabets = [cards[i][1] for i in range(4)]
    cnt = Counter(alphabets)
    if 2 in cnt.values():
        return False

    for i in range(4):
        if cnt[alphabets[i]] >= 3:
            pivot_alphabet = alphabets[i]
            break
    numbers = [int(cards[i][0]) for i in range(4) if cards[i][1] == pivot_alphabet]
    numbers = list(set(numbers))
    if len(numbers) < 3:
        return False
    numbers.sort()
    if len(numbers) == 3:
        if is_true(numbers):
            return True
    else:
        if is_true(numbers[:3]) or is_true(numbers[1:]):
            return True

    return False


def rule2(cards):
    # 적힌 알파벳과 숫자가 모두 같은 세 장이 존재.
    if cards[0] == cards[1] == cards[2] or cards[0] == cards[1] == cards[3] \
      or cards[0] == cards[2] == cards[3] or cards[1] == cards[2] == cards[3]:
        return True
    return False


def rule3(cards):
    # 두 장씩 짝지었을 때, 짝을 지은 카드끼리 적힌 숫자와 알파벳이 똑같을 때
    cnt = Counter(cards)
    if list(cnt.values()) == [2, 2]:
        return True
    return False


T = int(input())
for _ in range(T):
    cards = list(input().rstrip().split())
    flag1 = rule1(cards)
    flag2 = rule2(cards)
    flag3 = rule3(cards)

    if flag1 or flag2 or flag3:
        print(":)")
    else:
        print(":(")