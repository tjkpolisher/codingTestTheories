K = int(input())
cipher = input()
remnant = len(cipher) % K
if remnant != 0:
    cipher += '0' * remnant
table = []
for i in range(len(cipher) // K):
    row = list(cipher[K * i: K * (i+1)])
    if (i + 1) % 2 == 1:
        table.append(row)
    else:
        table.append(row[::-1])
answer = ''
for i in range(K):
    for j in range(len(table)):
        answer += table[j][i]
while '0' in answer:
    answer.strip('0')
print(answer)