from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine).most_common()
    result = 0
    
    for i, j in count:
        k -= j
        result += 1
        if k <=0:
            return result