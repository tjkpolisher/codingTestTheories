from itertools import combinations
N = int(input())
pictures = []
for _ in range(N):
    picture = ''
    for i in range(5):
        string_i = input()
        picture += string_i
    pictures.append(picture)

picture_index = list(range(N))
combs = list(combinations(picture_index, 2))

counters = []
for comb in combs:
    p1, p2 = pictures[comb[0]], pictures[comb[1]]
    counter = 0
    for i in range(5 * 7):
        if p1[i] != p2[i]:
            counter += 1
    counters.append(counter)
    
min_index = counters.index(min(counters))
p1, p2 = combs[min_index][0], combs[min_index][1]
print(p1 + 1, p2 + 1)