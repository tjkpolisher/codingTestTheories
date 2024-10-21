n = int(input())
citations = list(map(int, input().split()))
q_index = 0

citations.sort(reverse=True)
for i, k in enumerate(citations):
    if i + 1 <= k:
        q_index = i + 1

print(q_index)