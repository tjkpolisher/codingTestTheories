t = int(input())
for _ in range(t):
    letter = input()
    length = int(len(letter) ** 0.5)
    letter_array = []

    for i in range(length):
        letter_array.append(list(letter[length * i:length * (i + 1)]))

    ans = []
    for i in range(length):
        for j in range(length):
            ans.append(letter_array[j][length - i - 1])

    print(''.join(ans))