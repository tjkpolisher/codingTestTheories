N = int(input())
strings = input()

cnt = {'B': 0, 'R': 0}
cnt[strings[0]] += 1
for i in range(1, N):
    if strings[i] != strings[i-1]:
        cnt[strings[i]] += 1

print(min(cnt['B'], cnt['R']) + 1)