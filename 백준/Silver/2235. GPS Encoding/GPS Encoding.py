import sys
input = sys.stdin.readline


def decode(s, i, cypher, dp):
    n = len(s)
    # 재귀 종료 조건: 문자열의 끝에 도달하면 cost는 0, 암호문은 빈 문자열
    if i == n:
        return (0, "")
    if i in dp:
        return dp[i]

    best_count = float("inf")  # 최소 글자 수
    best_enc = ""  # 해당되는 암호문(사전 순으로 뒤쪽에 있는 것)

    # Case 1 - 한 자리 숫자일 떄
    num1 = int(s[i])
    next_count, next_enc = decode(s, i + 1, cypher, dp)
    candidate_count = next_count + 1
    candidate_enc = cypher[num1] + next_enc

    best_count = candidate_count
    best_enc = candidate_enc

    # Case 2 - 두 자리 숫자일 때(10 ~ 25)
    if i + 1 < n:
        two_digit = int(s[i:i + 2])
        if two_digit < 26:
            next_count2, next_enc2 = decode(s, i + 2, cypher, dp)
            candidate_count2 = 1 + next_count2
            candidate_enc2 = cypher[two_digit] + next_enc2

            if candidate_count2 < best_count:
                best_count = candidate_count2
                best_enc = candidate_enc2
            elif candidate_count2 == best_count and candidate_enc2 > best_enc:
                best_enc = candidate_enc2

    dp[i] = (best_count, best_enc)
    return dp[i]


problem_num = 1
while True:
    cypher = input().rstrip()
    if cypher == '#':
        break
    else:
        if problem_num > 1:
            # 문제와 문제 사이를 공백으로 구분(첫 문제는 제외)
            print()

    char_dict = {cypher[i]: i for i in range(26)}

    print(f"Problem {problem_num}")

    while True:
        num = input().rstrip()
        if num == '0':
            break

        dp = {}
        _, result = decode(num, 0, cypher, dp)
        print(result)

    problem_num += 1