from collections import Counter
def solution(str1, str2):    
    str1 = str1.upper()
    str2 = str2.upper()
    
    # 두 글자씩 끊어서 영문자로만 된 쌍 추출
    list1 = []
    for i in range(len(str1) - 1):
        frag = str1[i:i+2]
        if frag[0].isalpha() and frag[1].isalpha():
            list1.append(frag)
    
    list2 = []
    for i in range(len(str2) - 1):
        frag = str2[i:i+2]
        if frag[0].isalpha() and frag[1].isalpha():
            list2.append(frag)
    
    # 다중집합 생성 (Counter 사용)
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    
    # 교집합: 각 원소별로 min(개수1, 개수2)
    intersection = counter1 & counter2
    # 합집합: 각 원소별로 max(개수1, 개수2)
    union = counter1 | counter2
    
    intersection_count = sum(intersection.values())
    union_count = sum(union.values())
    
    # 둘 다 공집합이면 1
    if union_count == 0:
        return 65536
    
    # 자카드 유사도 계산
    jaccard = intersection_count / union_count
    return int(jaccard * 65536)