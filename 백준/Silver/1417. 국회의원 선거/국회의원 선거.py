N = int(input())
votes = []
for _ in range(N):
    votes.append(int(input()))

cnt = 0
while True:
    max_votes = max(votes)
    max_indices = []
    
    for i, v in enumerate(votes):
        if v == max_votes:
            max_indices.append(i)
        if len(max_indices) == votes.count(max_votes):
            break
    
    if len(max_indices) == 1:
        max_index = max_indices[0]
        if max_index == 0:
            print(cnt)
            break
        elif len(max_indices) == 1:
            votes[max_index] -= 1
            votes[0] += 1
            cnt += 1
    else:
        if 0 not in max_indices:
            max_index = max_indices[0]
        else:
            max_index = max_indices[1]
        
        votes[max_index] -= 1
        votes[0] += 1
        cnt += 1
