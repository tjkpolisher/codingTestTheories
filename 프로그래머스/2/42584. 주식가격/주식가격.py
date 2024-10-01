def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        price = prices[i]
        for j in range(i + 1, len(prices)):
            cnt += 1
            if price > prices[j]:
                break
        answer.append(cnt)
    return answer