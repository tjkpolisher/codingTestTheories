import sys
input = sys.stdin.readline

N, game_type = input().rstrip().split()

N = int(N)
game_members = {'Y': 2, 'F': 3, 'O': 4}
n_members = game_members[game_type]
names = set()

for _ in range(N):
    name = input().rstrip()
    names.add(name)

print(len(names) // (n_members - 1))