import sys
input = sys.stdin.readline

N = int(input())
A_list = list(map(int, input().split()))
A = {i + 1: A_list[i] for i in range(N)}  # 수도꼭지 번호는 1부터 시작
toggled = {i + 1: 0 for i in range(N)}  # 토글 시 원래 유량을 저장할 딕셔너리
Q = int(input())

ans = sum(A_list)   # 아무 조작도 하지 않았을 때 분당 탱크에 담기는 물의 양
print(ans)
for _ in range(Q):
    control = input().rstrip()
    if control.startswith('1'):
        n, i, x = control.split()
        i, x = int(i), int(x)
        if A[i]:
            # 수도꼭지가 열려 있는 경우
            ans += (x - A[i])
            A[i] = x
        else:
            # 수도꼭지가 잠겨 있는 경우
            toggled[i] = x
    else:
        n, i = control.split()
        i = int(i)
        if A[i]:
            # 수도꼭지가 열려 있는 경우
            toggled[i] = A[i]
            ans -= A[i]
            A[i] = 0
        else:
            # 수도꼭지가 잠겨 있는 경우
            A[i] = toggled[i]
            ans += A[i]
            toggled[i] = 0
    print(ans)