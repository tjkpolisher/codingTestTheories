import sys
input = sys.stdin.readline

m, b, s = map(int, input().split())
m -= 1

bus_routes = [list(input().rstrip()) for _ in range(b)]

stops = set()

for route in bus_routes:
    if route[m] == '1':
        for i in range(s):
            if route[i] == '1' and i != m:
                stops.add(i)

print(len(stops))