def solution(id_pw, db):
    for idset in db:
        if idset[0] != id_pw[0]:
            continue
        else:
            if idset[1] == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
        
    return "fail"