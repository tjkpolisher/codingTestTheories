import sys
input = sys.stdin.readline

B, C, D = map(int, input().split())
burgers = list(map(int, input().split()))
sides = list(map(int, input().split()))
beverages = list(map(int, input().split()))

print(sum(burgers) + sum(sides) + sum(beverages))

ans = 0
n = max((B, C, D))
burgers.sort(reverse=True)
sides.sort(reverse=True)
beverages.sort(reverse=True)


def append_none(list_element, n):
    if len(list_element) == n:
        return
    for _ in range(n - len(list_element)):
        list_element.append(0)


append_none(burgers, n)
append_none(sides, n)
append_none(beverages, n)

table = [burgers, sides, beverages]
none_flag = False
for i in range(n):
    tmp = 0
    for j in range(3):
        tmp2 = table[j][i]
        if tmp2 == 0 and not none_flag:
            none_flag = True
        tmp += tmp2
    if none_flag:
        ans += tmp
    else:
        ans += int(tmp * 0.9)

print(ans)