def change(cash):
    """`change`
    거스름돈으로 거슬러 줘야 할 동전의 최소 개수를 구하는 함수.  
    거스름돈으로 사용할 동전은 500원, 100원, 50원, 10원이며 모든 동전은 종류마다 무한히 존재한다고 가정합니다.
    ===========================================
    
    Input
        - cash: 손님에게 줘야 하는 거스름돈의 액수.
    
    Output
        - minimum: 거스름돈의 액수를 만들 수 있는 동전의 총 개수.
    """
    minimum = 0
    coins = [500, 100, 50, 10]
    for coin in coins:
        minimum += cash // coin
        cash %= coin
    return minimum

if __name__=="__main__":
    print(change(1260))