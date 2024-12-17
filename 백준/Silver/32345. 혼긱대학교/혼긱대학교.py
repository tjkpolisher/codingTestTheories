import sys
input = sys.stdin.readline

T = int(input())
vowels = {'a', 'e', 'i', 'o', 'u'}  # 'y'는 이 문제에서 모음으로 취급하지 않음
MOD = 10 ** 9 + 7

for _ in range(T):
    word = list(input().rstrip())
    ans = 1
    vowel_position = []

    for i, ch in enumerate(word):
        if ch in vowels:
            vowel_position.append(i)

    if not vowel_position:
        print(-1)
        continue

    for i in range(len(vowel_position) - 1):
        ans *= vowel_position[i + 1] - vowel_position[i]
    print(ans % MOD)