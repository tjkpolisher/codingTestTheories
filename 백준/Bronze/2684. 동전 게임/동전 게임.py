P = int(input())
three_coins = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH'] # 3-동전수열에 해당하는 각 8개 케이스에 대한 문자열
for _ in range(P):
    cnt = [0] * 8
    case = input()
    if case.count('H') == 40:
        cnt[-1] = 38
    elif case.count('T') == 40:
        cnt[0] = 38
    else:
        for i in range(38):
            c = case[i:i + 3]
            idx = three_coins.index(c)
            cnt[idx] = cnt[idx] + 1
    print(cnt[0], cnt[1], cnt[2], cnt[3], cnt[4], cnt[5], cnt[6], cnt[7])