def solution(record):
    uid_nickname_table = {}
    log_table = {}
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