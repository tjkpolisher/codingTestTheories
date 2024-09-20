A, B = map(int, input().split())
total = 9 * 17  # 총 경우의 수

if A == B:
    num = total - 10 + A
else:
    score = (A + B) % 10
    num = 0
    for i in range(1, 11):
        for j in range(i + 1, 11):
            if score > (i + j) % 10:
                if i == A and j == B:
                    continue
                elif i == A or j == A or i == B or j == B:
                    num += 2
                else:
                    num += 4

print(f"{num / total:.3f}")