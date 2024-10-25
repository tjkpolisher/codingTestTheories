N = int(input())
factorial = [1, 1]
for i in range(2, 21):
    factorial.append(factorial[-1] * i)

result = 0
for i in range(20, -1, -1):
    if result + factorial[i] < N:
        result += factorial[i]
    elif result + factorial[i] == N:
        print("YES")
        break
else:
    print("NO")