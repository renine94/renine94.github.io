from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            j = i + 1
            while j != len(nums):
                if num + nums[j] == target:
                    return [i, j]
                j += 1



nums = [3, 2, 4]
target = 6
Solution().twoSum(nums, target)