class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}

        for index, num in enumerate(nums):
            if target - num in pair:
                return [pair[target-num], index]
            pair[num] = index
        return []
