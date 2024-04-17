N = int(input())
clients = []
for i in range(N):
    age, name = input().split()
    clients.append([i, int(age), name])

clients.sort(key=lambda x: (x[1], x[0]))
for i in range(N):
    print(clients[i][1], clients[i][2])