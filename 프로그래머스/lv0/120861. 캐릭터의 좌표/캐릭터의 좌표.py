def solution(keyinput, board):
    result = [0,0]
    for key in keyinput:
        if key == 'left':
            result[0] = result[0]-1
            if result[0] < -(board[0]//2):
                result[0] += 1
        if key == 'right':
            result[0] = result[0]+1
            if result[0] > board[0]//2:
                result[0] -= 1
            
        if key == 'down':
            result[1] = result[1]-1
            if result[1] < -(board[1]//2):
                result[1] += 1
        if key == 'up':
            result[1] = result[1]+1
            if result[1] > board[1]//2:
                result[1] -= 1
    return result