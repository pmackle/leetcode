# Naive implementation
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, outer in enumerate(nums):
            for j, inner in enumerate(nums[i+1:], i+1):
                sum = outer + inner
                if sum == target:
                    return [i, j]