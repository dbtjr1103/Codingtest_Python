def solution(k, m, score):
    score.sort(reverse=True)
    apples_per_box = m
    boxes_sold = 0
    max_profit = 0
    i = 0

    while i < len(score):
        box_scores = score[i:i+apples_per_box]
        if not box_scores:
            break
        lowest_score = box_scores[-1]
        i += apples_per_box
        if len(box_scores) < apples_per_box:
            continue
        boxes_sold += 1
        max_profit += lowest_score * apples_per_box

    return max_profit
