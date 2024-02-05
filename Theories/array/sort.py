def solution(array):
    array.sort()
    return array

if __name__=="__main__":
    ex1 = [1, -5, 2, 4, 3]
    ex2 = [2, 1, 1, 3, 2, 5, 4]
    ex3 = [6, 1, 7]
    examples = [ex1, ex2, ex3]
    for e in examples:
        print(solution(e))