import math

def prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0

    for i in range(len(nums)-2):
        for m in range(i+1, len(nums)-1):
            for n in range(m+1, len(nums)):
                if prime(nums[i] + nums[m] + nums[n]):
                    answer += 1

    return answer
