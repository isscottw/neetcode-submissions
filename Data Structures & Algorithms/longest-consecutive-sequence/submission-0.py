class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        for num in nums_set:
            if num - 1 not in nums_set:
                count = 1
                while num + 1 in nums_set:
                    count += 1
                    num += 1
                if count >= max_count:
                    max_count = count
        return max_count
