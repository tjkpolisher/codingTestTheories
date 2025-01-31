from collections import Counter
def solution(X, Y):
    if not set(X).intersection(set(Y)):
        # 겹치는 글자가 아예 없는 경우
        return '-1'

    answer = []
    # X와 Y에 포함된 각 숫자의 개수 카운팅
    X_counter = Counter(X)
    Y_counter = Counter(Y)

    for i in range(9, -1, -1):
        key = str(i)
        if key in X_counter.keys() and key in Y_counter.keys():
            cnt = min(X_counter[key], Y_counter[key])
            for _ in range(cnt):
                answer.append(key)
    if set(answer) == {"0"}:
        return "0"
    return ''.join(answer)
        