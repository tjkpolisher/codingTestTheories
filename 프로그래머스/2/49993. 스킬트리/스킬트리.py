def solution(skill, skill_trees):
    answer = 0
    skill_characters = set(skill)
    
    for skill_tree in skill_trees:
        i = 0  # skill의 문자 인덱스
        for ch in skill_tree:
            if ch not in skill_characters:
                continue
            elif ch == skill[i]:
                i += 1
            else:
                break
        else:
            answer += 1
    
    return answer