string = input()
alphabet_key = list("abcdefghijklmnopqrstuvwxyz")
alphabet_value = [0] * len(alphabet_key)
alphabet = {alphabet_key[i]:alphabet_value[i] for i in range(len(alphabet_key))}
for c in string:
    alphabet[c] += 1
for i in range(len(alphabet_key)):
    print(alphabet[alphabet_key[i]], end=' ')