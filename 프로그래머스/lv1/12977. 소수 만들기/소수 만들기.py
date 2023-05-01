def solution(nums):
    answer = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                number = nums[i] + nums[j] + nums[k]
                if len([m for m in range(2, number) if number % m == 0]) == 0:
                    answer += 1

    return answer