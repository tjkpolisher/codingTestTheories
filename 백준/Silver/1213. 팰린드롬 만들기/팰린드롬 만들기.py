import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def odd_counter(d):
    odd_counter = 0
    odd_key = ''
    for key in d:
        if d[key] % 2 == 1:
            odd_counter += 1
            odd_key = key
        if odd_counter >= 2:
            return True, ''
    return False, odd_key


def palindrome(name):
    alphabet_dict = defaultdict(int)
    for c in name:
        alphabet_dict[c] += 1

    is_odd, odd_key = odd_counter(alphabet_dict)
    if is_odd:
        return "I'm Sorry Hansoo"

    palindrome = deque()
    if odd_key:
        palindrome.append(odd_key)
        alphabet_dict[odd_key] -= 1

    sorted_keys = sorted(alphabet_dict.keys(), reverse=True)
    for key in sorted_keys:
        count = alphabet_dict[key]
        for _ in range(count // 2):
            palindrome.appendleft(key)
            palindrome.append(key)

    return ''.join(palindrome)


name = input().rstrip()
print(palindrome(name))