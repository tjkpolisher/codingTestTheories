import sys
input = sys.stdin.readline

alphabet_table = {chr(i + 65): i + 1 for i in range(26)}

original = input().rstrip()
biznerre = input().rstrip()


def to_list(string):
    return [alphabet_table[c] for c in string]


def decypher(n, b):
    diff = b - n
    if diff <= 0:
        diff += 26
    return diff


original_list = to_list(original)
biznerre_list = to_list(biznerre)

key = []
for i in range(len(original)):
    key.append(chr(64 + decypher(original_list[i], biznerre_list[i])))

ans_tmp = ''.join(key)

n = len(original)
for i in range(1, n // 2 + 1):
    if n % i != 0:
        continue

    repeat_str = ans_tmp[:i]
    if repeat_str * (n // i) == ans_tmp:
        print(repeat_str)
        break
else:
    print(ans_tmp)