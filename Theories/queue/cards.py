def solution(cards1, cards2, goal):
    # 문제 출처: 프로그래머스 연습문제 - 카드 뭉치
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/159994
    from collections import deque
    deque1 = deque()
    deque2 = deque()
    for word in goal:
        if word in cards1:
            deque1.append(word)
        elif word in cards2:
            deque2.append(word)
    if list(deque1) == cards1 and list(deque2) == cards2:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    ex1 = [["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]]
    ex2 = [["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]]
    for e in [ex1, ex2]:
        print(solution(e[0], e[1], e[2]))