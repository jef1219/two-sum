from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    break_check = True
                    return [j,i]
