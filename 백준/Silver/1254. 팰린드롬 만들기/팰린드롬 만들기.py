S = input()
length = len(S)

for i in range(length):
    if S[i:] == S[i:][::-1]:
        print(length + i)
        break