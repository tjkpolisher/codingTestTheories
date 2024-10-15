import sys
input = sys.stdin.readline

while True:
    sequence = list(map(int, input().split()))
    if not sequence:
        break
    n = sequence[0]
    sequence.remove(n)

    if len(sequence) == 1:
        print("Jolly")
    else:
        differences = set(range(1, n))  # 연속된 두 수의 차의 절대값을 비교
        for i in range(n - 1):
            diff = abs(sequence[i] - sequence[i + 1])
            if diff not in differences:
                print("Not jolly")
                break
            differences.remove(diff)
        else:
            if not differences:
                print("Jolly")
            else:
                print("Not jolly")