def solution(numbers):
    answer = []
    n = len(numbers)
    for i in range(n-1):
        for j in range(i+1, n):
            num = numbers[i] + numbers[j]
            if num not in answer:
                answer.append(num)
    return sorted(answer)