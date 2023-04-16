def solution(dots):
    
    x, y = [], [] 

    for dot in dots:
        x.append(dot[0])
        y.append(dot[1])
        
    w = max(x) - min(x)
    h = max(y) - min(y)
    
    return w * h