class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time: O(n) Space: O(1)
        l, r = 0, len(numbers) - 1
        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum == target:
                return [l + 1, r + 1]
            if cur_sum < target:
                l += 1
            else:
                r -= 1
        return []
