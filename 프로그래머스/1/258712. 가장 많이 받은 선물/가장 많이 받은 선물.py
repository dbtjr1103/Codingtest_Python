def solution(friends, gifts):
    # 친구들의 이름과 인덱스 매핑
    name2idx = {name: idx for idx, name in enumerate(friends)}
    name2factor = {name: 0 for name in friends}
    arr = [[0 for _ in range(len(friends))] for _ in range(len(friends))]

    # 선물 기록 처리
    for gift in gifts:
        giver, receiver = gift.split()
        name2factor[giver] += 1
        name2factor[receiver] -= 1
        arr[name2idx[giver]][name2idx[receiver]] += 1

    # 다음 달 선물 예측
    v = [0 for _ in range(len(friends))]
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if arr[i][j] > arr[j][i]:
                v[i] += 1
            elif arr[i][j] < arr[j][i]:
                v[j] += 1
            else:
                if name2factor[friends[i]] > name2factor[friends[j]]:
                    v[i] += 1
                elif name2factor[friends[i]] < name2factor[friends[j]]:
                    v[j] += 1

    # 결과 반환
    return max(v)