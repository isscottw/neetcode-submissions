class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: O(n) Space: O(n)
        streak = defaultdict(int)
        longest = 0
        for num in nums:
            if not streak[num]:
                streak[num] = streak[num - 1] + 1 + streak[num + 1]
                streak[num - streak[num - 1]] = streak[num]
                streak[num + streak[num + 1]] = streak[num]
                longest = max(longest, streak[num])
        return longest
