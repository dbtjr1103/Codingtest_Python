def solution(dots):
    x1, y1 = dots[0]
    x2, y2 = dots[1]
    x3, y3 = dots[2]
    x4, y4 = dots[3]

    # 세 쌍의 직선에 대한 기울기 계산
    def calc_slope(x1, y1, x2, y2):
        if x2 - x1 == 0:  # 분모가 0인 경우를 처리
            return float('inf')
        return (y2 - y1) / (x2 - x1)

    slope1 = calc_slope(x1, y1, x2, y2)
    slope2 = calc_slope(x3, y3, x4, y4)

    # 세 쌍의 기울기가 같은지 확인
    if slope1 == slope2:
        return 1

    slope1 = calc_slope(x1, y1, x3, y3)
    slope2 = calc_slope(x2, y2, x4, y4)

    if slope1 == slope2:
        return 1

    slope1 = calc_slope(x1, y1, x4, y4)
    slope2 = calc_slope(x2, y2, x3, y3)

    if slope1 == slope2:
        return 1

    return 0

