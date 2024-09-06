N, score_new, P = map(int, input().split())
try:
    score_list = list(map(int, input().split()))

    ans = 1
    for score in score_list:
        if score > score_new:
            ans += 1
        elif score == score_new:
            continue
        else:
            break

    if N < P or (N == P and score_new > score_list[-1]):
        print(ans)
    else:
        print(-1)
except:
    print(1)