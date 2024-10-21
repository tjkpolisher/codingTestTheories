N = int(input())
ans = 0
n1, n2, n3 = 0, 0, 0  # 택희, 남규, 영훈이 받을 사탕의 개수

for i in range(1, N + 1):  # 택희가 받을 사탕
    if i % 2 != 0:  # 택희는 짝수 개의 사탕을 받음
        continue
    for j in range(1, N - i + 1):  # 남규가 받을 사탕
        n = N - i - j  # 영훈이 받을 사탕(전체 사탕을 남김없이 분배해야 함)
        if n <= 0:  # 남규와 영훈은 최소 1개의 사탕을 받아야 함
            continue
        if j - n < 2:  # 남규는 영훈이보다 2개 이상 많은 사탕을 가져야 함
            continue
        ans += 1

print(ans)