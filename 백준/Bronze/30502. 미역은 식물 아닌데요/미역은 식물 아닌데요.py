N, M = map(int, input().split())
creatures = dict()
plant_min = 0
plant_max = 0

for _ in range(M):
    a, b, c = input().split()
    a, c = map(int, (a, c))
    if a not in creatures:
        creatures[a] = {'P': -1, 'M': -1}
    creatures[a][b] = c

for c in creatures.values():
    if c['P'] == 1 and c['M'] == 0:
        plant_min += 1
        plant_max += 1
    elif c['P'] == 0 or c['M'] == 1:
        pass
    else:
        plant_max += 1

plant_max += (N - len(creatures))

print(plant_min, plant_max)