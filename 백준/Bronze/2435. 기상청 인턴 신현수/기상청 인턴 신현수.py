N, K = map(int, input().split())
seq = list(map(int, input().split()))
seq_ans = []
for i in range(N - K + 1):
    seq_ans.append(sum(seq[i:i + K]))
print(max(seq_ans))