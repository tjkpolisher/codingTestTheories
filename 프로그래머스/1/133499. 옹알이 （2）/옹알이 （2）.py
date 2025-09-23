from collections import deque
def solution(babbling):
    pronounciation = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for babb in babbling:
        # 길이가 1이면 맞는 발음이 없으므로 continue
        if len(babb) < 2:
            continue
        babb_q = deque(list(babb))
        is_not = False  # 루프 종료 플래그
        previous_pro = None  # 이전에 말한 발음 (같은 발음 연속 불가)
        
        # 발음 비교
        while babb_q:
            print(f"{babb_q=}")
            if is_not:
                break

            for i in range(4):
                pro = pronounciation[i]
                len_pro = len(pro)
                print(f"{pro=}")
                
                if len(babb_q) < len_pro:
                    continue
                
                # 연속된 발음 불가
                if ''.join(list(babb_q)[:len_pro]) == previous_pro:
                    is_not = True
                    break

                # 앞에서 len_pro개 만큼의 글자가 pro와 일치하는지 확인 
                if pro == ''.join(list(babb_q)[:len_pro]):
                    for _ in range(len_pro):
                        babb_q.popleft()
                    previous_pro = pro  # 이전 발음 갱신
                    break
            else:  # 일치하는 발음이 없는 경우
                is_not = True  # 플래그를 True로 설정
            # print(f"{is_not=}")
            # print()
        
        if not babb_q and is_not == False:  # 옹알이 큐가 비어 있고 플래그가 False로 남아있는 경우
            answer += 1
    #         t.append(babb)
    # print(f"{t=}")
    return answer