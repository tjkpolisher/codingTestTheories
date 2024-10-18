N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]
answer = 0

# 정답에 맞는 세 자리 수의 자릿수 별로 탐색
for a in range(1, 10):  # 백의 자리
    for b in range(1, 10):  # 십의 자리
        for c in range(1, 10):  # 일의 자리
            cnt = 0

            # 세 자리 수를 정확하게 맞추어 3 스트라이크가 되면 게임 종료
            if a == b or b == c or c == a:
                continue
            for array in numbers:
                check = list(str(array[0]))
                strike = int(array[1])
                ball = int(array[2])

                strike_count = 0
                ball_count = 0

                if a == int(check[0]):
                    strike_count += 1
                if b == int(check[1]):
                    strike_count += 1
                if c == int(check[2]):
                    strike_count += 1

                if a == int(check[1]) or a == int(check[2]):
                    ball_count += 1
                if b == int(check[0]) or b == int(check[2]):
                    ball_count += 1
                if c == int(check[0]) or c == int(check[1]):
                    ball_count += 1

                if strike != strike_count:
                    break
                if ball != ball_count:
                    break

                cnt += 1

            if cnt == N:
                answer += 1

print(answer)