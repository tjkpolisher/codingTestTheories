def solution(want, number, discount):
    # 문제 출처: 프로그래머스 연습문제 - 할인 행사
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/131127
    want_table = {want[i] : number[i] for i in range(len(want))}
    cnt = 0
    
    for i in range(len(discount) - 9):
        dc_sliced = discount[i:i+10]
        dc_table = {dc_sliced[j] : dc_sliced.count(dc_sliced[j]) for j in range(len(dc_sliced))}
        if dc_table == want_table:
            cnt += 1
    
    return cnt

if __name__ == "__main__":
    ex1 = [["banana", "apple", "rice", "pork", "pot"],
           [3, 2, 2, 2, 1],
           ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]]
    ex2 = [["apple"],
           [10],
           ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]]
    
    for e in [ex1, ex2]:
        print(solution(e[0], e[1], e[2]))
