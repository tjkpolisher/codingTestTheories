def solution(participant, completion):
    # 문제 출처: 프로그래머스 해시 - 완주하지 못한 선수
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42576
    complete_table = {}
    
    for p in participant:
        if p in complete_table:
            complete_table[p] += 1
        else:
            complete_table[p] = 1
    
    for c in completion:
        complete_table[c] -= 1
    
    for key in complete_table.keys():
        if complete_table[key] > 0:
            return key

if __name__ == "__main__":
    ex1 = [["leo", "kiki", "eden"], ["eden", "kiki"]]
    ex2 = [["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]]
    ex3 = [["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]]
    for e in [ex1, ex2, ex3]:
        print(solution(e[0], e[1]))
