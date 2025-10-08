def solution(numbers, hand):
    answer = []
    left_column = {1: 0, 4: 1, 7: 2, '*': 3}
    central_column = {2: 0, 5: 1, 8: 2, 0: 3}
    right_column = {3: 0, 6: 1, 9: 2, '#': 3}
    
    # 양 엄지 손가락의 현위치(행, 열 순서)
    left_thumb = [3, 0]
    right_thumb = [3, 2]
    
    for number in numbers:
        # idx1: 행, idx2: 열
        if number in left_column:  # 1, 4, 7 입력 시
            idx1 = left_column[number]
            idx2 = 0
            
            answer.append('L')
            left_thumb = [idx1, idx2]
        elif number in central_column:  # 2, 5, 8, 0 입력 시
            idx1 = central_column[number]
            idx2 = 1
            
            # 왼쪽/오른쪽 엄지손가락에서 버튼까지의 맨해튼 거리
            left_distance = abs(left_thumb[0] - idx1) + abs(left_thumb[1] - idx2)
            right_distance = abs(right_thumb[0] - idx1) + abs(right_thumb[1] - idx2)
            
            if left_distance == right_distance:  # 두 거리가 같을 경우 주 손 이용
                if hand == 'left':
                    answer.append('L')
                    left_thumb = [idx1, idx2]
                else:
                    answer.append('R')
                    right_thumb = [idx1, idx2]
            # 그렇지 않을 경우 더 가까운 손가락 이용
            elif left_distance < right_distance:
                answer.append('L')
                left_thumb = [idx1, idx2]
            else:
                answer.append('R')
                right_thumb = [idx1, idx2]
        else:  # 3, 6, 9 입력 시
            idx1 = right_column[number]
            idx2 = 2
            
            answer.append('R')
            right_thumb = [idx1, idx2]
        
    return ''.join(answer)