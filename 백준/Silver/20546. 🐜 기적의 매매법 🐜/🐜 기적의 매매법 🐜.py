cash_now = int(input())
stocks = list(map(int, input().split()))


def bnp(start, stocks):
    for i in range(14):
        if stocks[i] <= start or i == 13:
            number, cash = divmod(start, stocks[i])
            break
    return cash + stocks[-1] * number


def timing(start, stocks):
    number, cash = 0, start
    for i in range(10):
        if stocks[i] < stocks[i + 1] < stocks[i + 2]:
            # 전량 매도 조건
            cash += number * stocks[i + 3]
            number = 0
        elif stocks[i] > stocks[i + 1] > stocks[i + 2]:
            # 전량 매수 조건
            number_new, cash = divmod(cash, stocks[i + 3])
            number += number_new
    return cash + stocks[-1] * number


asset_bnp = bnp(cash_now, stocks)
asset_timing = timing(cash_now, stocks)
# print(f"{asset_bnp=}, {asset_timing=}")
if asset_bnp == asset_timing:
    print("SAMESAME")
elif asset_bnp > asset_timing:
    print("BNP")
else:
    print("TIMING")