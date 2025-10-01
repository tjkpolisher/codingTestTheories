sentence = input()
answer = []
vowels = {'a', 'e', 'i', 'o', 'u'}
i = 0
while i < len(sentence):
    answer.append(sentence[i])
    if sentence[i] in vowels:
        i += 3
    else:
        i += 1

print(''.join(answer))