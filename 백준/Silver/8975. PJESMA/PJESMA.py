from math import ceil
import sys
input = sys.stdin.readline

N = int(input())
titles = {}
for _ in range(N):
    titles[input().rstrip()] = False

M = int(input())
lyrics = []
for _ in range(M):
    lyrics.append(input().rstrip())

cnt = 0
for i in range(M):
    word = lyrics[i]
    if word in titles and not titles[word]:
        cnt += 1
        titles[word] = True
    if cnt >= ceil(N / 2):
        print(i + 1)
        break