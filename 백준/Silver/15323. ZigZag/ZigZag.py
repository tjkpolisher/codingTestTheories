import sys
from collections import deque
input = sys.stdin.readline

K, N = map(int, input().rstrip().split())
words = [input().rstrip() for _ in range(K)]
letters = [input().rstrip() for _ in range(N)]

word_dict = {}
distinct_letter = list(set(letters))
for word in words:
    first_letter = word[0]
    if first_letter not in word_dict:
        word_dict[first_letter] = []
    word_dict[first_letter].append(word)

for letter in distinct_letter:
    word_dict[letter] = deque(sorted(word_dict[letter]))

for letter in letters:
    word_to_print = word_dict[letter].popleft()
    print(word_to_print)
    word_dict[letter].append(word_to_print)