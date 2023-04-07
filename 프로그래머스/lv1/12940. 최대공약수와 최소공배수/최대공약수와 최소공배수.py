import math

def solution(n, m):
    # 최소공배수 = 두 자연수의 곱 / 최대공약수    
    answer = []
    answer.append(math.gcd(n, m))
    answer.append(n*m/answer[0])

    return answer