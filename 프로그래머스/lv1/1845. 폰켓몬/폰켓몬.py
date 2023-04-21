def solution(nums: list) -> int:
    return min(len(set(nums)), len(nums) // 2)