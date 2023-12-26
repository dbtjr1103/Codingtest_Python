def solution(bandage, health, attacks):
    # 붕대 감기 기술 정보 추출: 시전 시간(t), 초당 회복량(x), 추가 회복량(y)
    t, x, y = bandage

    # 현재 체력과 연속 성공 시간 초기화
    current_health = health
    consecutive_success = 0

    # 마지막 공격 시간 계산
    last_attack_time = max(attacks, key=lambda a: a[0])[0]

    # 시간별로 캐릭터의 상태를 시뮬레이션
    for second in range(last_attack_time + 1):
        # 해당 시간에 몬스터의 공격이 있는지 확인
        if any(attack[0] == second for attack in attacks):
            # 공격이 있는 경우, 연속 성공 시간 초기화 및 체력 감소
            consecutive_success = 0
            attack_damage = next(attack[1] for attack in attacks if attack[0] == second)
            current_health -= attack_damage

            # 체력이 0 이하가 되면 -1을 반환
            if current_health <= 0:
                return -1
        else:
            # 공격이 없는 경우, 체력 회복
            # 최대 체력을 초과하지 않도록 조정
            current_health = min(health, current_health + x)
            consecutive_success += 1

            # 연속 성공 시간이 시전 시간에 도달하면 추가 회복
            if consecutive_success == t:
                current_health = min(health, current_health + y)
                consecutive_success = 0  # 연속 성공 시간 초기화

    # 모든 공격이 끝난 후 남은 체력 반환
    return current_health
