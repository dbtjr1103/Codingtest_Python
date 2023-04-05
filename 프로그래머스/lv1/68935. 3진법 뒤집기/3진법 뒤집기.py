def solution(n):
    three = ''
    
    while n > 0:
        n, mod = divmod(n, 3)
        three += str(mod)
        
    # int(three[::-1])
    answer = int(three,3)
    
    return answer