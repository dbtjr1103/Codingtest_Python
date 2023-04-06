def solution(number):
    
    from itertools import combinations

    trio = list(combinations(number, 3))
    count = 0
    for i in trio:
        if sum(i) == 0:
            count += 1
    
    return count