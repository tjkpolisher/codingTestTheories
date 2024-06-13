price = int(input())
change = 1000 - price
change_list = [500, 100, 50, 10, 5, 1]
answer = 0
for c in change_list:
    n1, n2 = divmod(change, c)
    answer += n1
    change = n2
print(answer)