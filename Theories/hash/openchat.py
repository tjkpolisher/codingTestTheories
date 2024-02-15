def solution(record):
    # 문제 출처: 2019 KAKAO BLIND RECRUITMENT - 오픈 채팅방
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42888

    uid_nickname_table = {}
    log_table = {}  # uid와 행동을 저장하는 딕셔너리
    log_list = []

    for i, log in enumerate(record):
        if log.startswith('Enter'):
            action, uid, nickname = log.split()
            uid_nickname_table[uid] = nickname
            log_table[i] = [uid, action]
        elif log.startswith('Leave'):
            action, uid = log.split()
            log_table[i] = [uid, action]
        elif log.startswith('Change'):
            action, uid, nickname = log.split()
            uid_nickname_table[uid] = nickname
            log_table[i] = [uid, action]

    for log in log_table.values():
        if log[1] == 'Enter':
            log_list.append(f"{uid_nickname_table[log[0]]}님이 들어왔습니다.")
        elif log[1] == 'Leave':
            log_list.append(f"{uid_nickname_table[log[0]]}님이 나갔습니다.")

    return log_list


if __name__ == "__main__":
    ex1 = ["Enter uid1234 Muzi",
           "Enter uid4567 Prodo",
           "Leave uid1234",
           "Enter uid1234 Prodo",
           "Change uid4567 Ryan"]
    print(solution(ex1))
