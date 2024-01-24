from collections import Counter

def solution(participant, completion):
    hash_map = Counter(participant)  # 참가자의 이름별 빈도수 계산
    for name in completion:
        hash_map[name] -= 1  # 완주한 선수의 빈도수 감소

    for name, count in hash_map.items():
        if count > 0:  # 완주하지 못한 선수 찾기
            return name