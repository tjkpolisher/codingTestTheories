import sys
input = sys.stdin.readline

N, M = map(int, input().split())
site_password = {}
for _ in range(N):
    site, password = input().rstrip().split()
    site_password[site] = password

for _ in range(M):
    site = input().rstrip()
    print(site_password[site])