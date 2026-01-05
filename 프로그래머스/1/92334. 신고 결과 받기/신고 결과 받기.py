from collections import defaultdict
def solution(id_list, report, k):
    length = len(id_list)
    reported = defaultdict(list)  # 계정별 신고한
    counter = {id_list[i]: 0 for i in range(length)}  # 계정별 신고당한 횟수
    unique_report = set()  # 고유한 신고 저장 집합
    suspended = set()  # 정지당한 계정
    
    report = list(set(report))  # 중복 신고 제거
    
    # 1. report 순회하면서 신고자-피신고자 식별
    for log in report:
        unique_report.add(log)
        name1, name2 = log.split()  # 신고자, 피신고자
        reported[name1].append(name2)
        
        counter[name2] += 1  # 신고당한 횟수에 1 더하기
        if counter[name2] >= k:
            suspended.add(name2)
    
    # 2. 완성된 reported 중 k회 이상 신고당한 횟수 추출
    answer = [0] * length
    for i, ids in enumerate(id_list):
        for name in reported[ids]:
            if name in suspended:
                answer[i] += 1
    return answer