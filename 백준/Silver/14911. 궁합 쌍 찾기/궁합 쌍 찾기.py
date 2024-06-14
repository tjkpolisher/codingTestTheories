numbers = list(map(int, input().split()))
integer = int(input())

numbers.sort()
answer = set()

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == integer:
            answer.add((numbers[i], numbers[j]))

answer = list(answer)
answer.sort()
for pair in answer:
    print(pair[0], pair[1])
print(len(answer))