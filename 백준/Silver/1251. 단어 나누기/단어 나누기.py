word = input()
length = len(word)
flipped = []

for i in range(1, length - 1):
    for j in range(1, length - i):
        p1 = word[:i]
        p2 = word[i:i + j]
        p3 = word[i + j:]
        flipped.append(p1[::-1] + p2[::-1] + p3[::-1])

flipped.sort()
print(flipped[0])