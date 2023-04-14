def solution(spell, dic):
    spell = set(spell)
    
    for i in dic:
        j = set(list(i))

        if len(spell) != len(j) :
            continue

        if j == spell:
            return 1 
        
    return 2