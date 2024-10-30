import sys
input = sys.stdin.readline

N = int(input())
HFM = []
for i in range(N):
    J_i, P_i = map(int, input().split())
    HFM.append([i, P_i, J_i/P_i])

HFM.sort(key=lambda x: x[2], reverse=True)
price = HFM[0][1] + HFM[1][1] + HFM[2][1]
print(price)
for i in range(3):
    print(HFM[i][0] + 1)