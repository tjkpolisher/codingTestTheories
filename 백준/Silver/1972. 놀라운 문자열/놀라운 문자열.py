def surprising(string, n):
    for j in range(1, n - 1):
        pairs = set()
        for i in range(n - j):
            pairs.add(''.join([string[i], string[i + j]]))
        if len(pairs) != N - j:
            return False
    return True


while True:
    string = input()
    if string == '*':
        break
    N = len(string)
    if surprising(string, N):
        print(f"{string} is surprising.")
    else:
        print(f"{string} is NOT surprising.")