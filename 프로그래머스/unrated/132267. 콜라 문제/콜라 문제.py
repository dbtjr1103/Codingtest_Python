def solution(a, b, n):
    
    answer, emp = 0,0
    while n >= a:
        k = n//a * b
        emp = n%a
        
        answer += k
        
        n =  n//a * b +emp

    return answer