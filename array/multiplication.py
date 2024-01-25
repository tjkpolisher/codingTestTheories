def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            answer[i][j] = sum([arr1[i][k] * arr2[k][j] for k in range(len(arr1[0]))])
    return answer

if __name__=="__main__":
    ex1 = [[[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]]
    ex2 = [[[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]]
    examples = [ex1, ex2]
    for e in examples:
        print(solution(e[0], e[1]))