def solution(score):
    
    # 평균 계산
    avg = [(s[0] + s[1]) / 2 for s in score]
    
    ranks = []
    for a in avg:
        rank = 1
        for b in avg:
            if a < b:
                rank +=1
        ranks.append(rank)
    
    return ranks