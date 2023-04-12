def solution(food):
    answer = ''
    for i in range(len(food)-1):
        n = food[i+1]//2
        answer += str(i+1)*n
    return answer + "0" + answer[::-1]