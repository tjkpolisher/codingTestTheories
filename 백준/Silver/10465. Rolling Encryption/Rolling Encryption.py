k = int(input())
string = input()

n = len(string)
if n <= k:
    print(string)
    exit()

ans = []
ans.append(string[:k])

freq = [0] * 26
for i in range(k):
    freq[ord(string[i]) - ord('a')] += 1

for i in range(k, n):
    max_cnt = max(freq)
    for idx in range(26):
        if freq[idx] == max_cnt:
            shift = idx + 1
            break

    orig_idx = ord(string[i]) - ord('a')

    enc_idx = (orig_idx + shift) % 26
    ans.append(chr(enc_idx + ord('a')))
    if i - k >= 0:
        out_idx = ord(string[i - k]) - ord('a')
        freq[out_idx] -= 1
    freq[orig_idx] += 1

print(''.join(ans))