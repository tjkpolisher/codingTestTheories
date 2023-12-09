def solution(keyinput, board):
    answer = [0, 0]
    x_thres = board[0] // 2
    y_thres = board[1] // 2
    keys = {'up':[0, 1], 'down':[0, -1],
           'left':[-1, 0], 'right':[1, 0]}
    for key in keyinput:
        answer = [answer[0] + keys[key][0], answer[1] + keys[key][1]]
        if answer[0] > x_thres:
            answer[0] = x_thres
        elif answer[0] < -x_thres:
            answer[0] = -x_thres
        
        if answer[1] > y_thres:
            answer[1] = y_thres
        elif answer[1] < -y_thres:
            answer[1] = -y_thres
    
    return answer