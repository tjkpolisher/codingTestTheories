def Collatz(n):
    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n //= 2
    return n


def find_meeting_point(A, B):
    # A와 B의 콜라츠 시퀀스에서 같은 수가 나타나는 첫 번째 지점을 찾는 함수
    steps_A, steps_B = {A: 0}, {B: 0}
    seq_A, seq_B = A, B
    step_count_A, step_count_B = 0, 0

    while True:
        if seq_A != 1:
            seq_A = Collatz(seq_A)
            step_count_A += 1
            if seq_A in steps_B:
                # A의 시퀀스가 B의 시퀀스에 이미 나타난 수를 만났을 때
                return A, step_count_A, B, steps_B[seq_A], seq_A
            steps_A[seq_A] = step_count_A

        if seq_B != 1:
            seq_B = Collatz(seq_B)
            step_count_B += 1
            if seq_B in steps_A:
                # B의 시퀀스가 A의 시퀀스에 이미 나타난 수를 만났을 때
                return A, steps_A[seq_B], B, step_count_B, seq_B
            steps_B[seq_B] = step_count_B

        if seq_A == 1 and seq_B == 1:
            # 두 시퀀스가 동시에 1에 도달했을 때
            break

    return A, steps_A[1], B, steps_B[1], 1


while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    if A == B:
        A, S_A, B, S_B, C = A, 0, B, 0, A
    else:
        A, S_A, B, S_B, C = find_meeting_point(A, B)

    print(f"{A} needs {S_A} steps, {B} needs {S_B} steps, they meet at {C}")
