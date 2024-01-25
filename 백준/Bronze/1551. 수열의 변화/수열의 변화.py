N, K = map(int, input().split())
seq = list(map(int, input().split(',')))
for _ in range(K):
    new_seq = []
    for i in range(len(seq) - 1):
        new_seq.append(seq[i + 1] - seq[i])
    seq = new_seq
for i in range(len(seq)):
    if i == len(seq) - 1:
        print(seq[i])
    else:
        print(seq[i], end=',')