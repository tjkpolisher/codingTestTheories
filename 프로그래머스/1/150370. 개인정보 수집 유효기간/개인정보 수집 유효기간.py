import datetime
def solution(today, terms, privacies):
    """
    # 입력
    today: 오늘 날짜(str), terms: 약관의 유효기간(1차원 str 배열), privacies: 수집된 개인정보(1차원 str 배열)
    
    # 출력
    answer: 파기해야 할 개인정보 번호를 오름차순으로 정렬한 1차원 int 배열
    """
    # [중요] 모든 달은 28일까지 있다고 가정
    answer = []
    
    # terms 리스트의 정보를 딕셔너리로 분리(키: 약관 종류, 값: 약관 유효기간)
    terms_dict = {}
    for term in terms:
        code, month = term.split()
        month = int(month)
        terms_dict[code] = month
        
    def to_days(date_str):
        y, m, d = map(int, date_str.split('.'))
        # (연 * 12 + (월-1)) * 28 + 일
        return (y * 12 + (m - 1)) * 28 + d
    
    # 수집된 개인정보를 순회하면서 유효기간 만료 여부 확인
    today_days = to_days(today)

    for i, privacy in enumerate(privacies):
        date_str, code = privacy.split()
        start_days = to_days(date_str)
        
        # 유효기간(개월)을 일수로 변환해서 더하고, 만료일은 그 전날까지만 보관하므로 -1
        expire_days = start_days + terms_dict[code] * 28 - 1

        if expire_days < today_days:
            answer.append(i + 1)
    
    return answer