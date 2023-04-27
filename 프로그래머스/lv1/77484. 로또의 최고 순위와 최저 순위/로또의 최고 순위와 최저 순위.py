def solution(lottos, win_nums):
    dic_rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    count = 0
    for i in lottos:
        if i in win_nums:
            count+=1
        
    num_max = count + lottos.count(0)
    num_min = count
    
    
    answer = [dic_rank[num_max], dic_rank[num_min]]
    return answer