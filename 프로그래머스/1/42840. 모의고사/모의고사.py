def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s1, s2, s3 = 0, 0, 0
    for i, n in enumerate(answers):
        if n == one[i % len(one)]:
            s1 += 1
        if n == two[i % len(two)]:
            s2 += 1
        if n == three[i % len(three)]:
            s3 += 1
    scores = [s1, s2, s3]
    max_score = max(scores)
    answer = [i + 1 for i in range(3) if max_score == scores[i]]
    if len(answer) >= 2:
        answer.sort()
    return answer