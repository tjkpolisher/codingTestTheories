def solution(data, ext, val_ext, sort_by):
    # 데이터 형식: ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]
    answer = []
    
    if ext == 'code':
        for datum in data:
            if datum[0] < val_ext:
                answer.append(datum)
    elif ext == 'date':
        for datum in data:
            if datum[1] < val_ext:
                answer.append(datum)
    elif ext == 'maximum':
        for datum in data:
            if datum[2] < val_ext:
                answer.append(datum)
    else:
        for datum in data:
            if datum[3] < val_ext:
                answer.append(datum)
    
    if sort_by == 'code':
        return sorted(answer, key=lambda x: x[0])
    elif sort_by == 'date':
        return sorted(answer, key=lambda x: x[1])
    elif sort_by == 'maximum':
        return sorted(answer, key=lambda x: x[2])
    else:
        return sorted(answer, key=lambda x: x[3])