def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = arr1[i] | arr2[i] # 비트 OR 연산 수행
        answer.append(format(tmp, 'b').zfill(n).replace('1','#').replace('0',' '))
    return answer