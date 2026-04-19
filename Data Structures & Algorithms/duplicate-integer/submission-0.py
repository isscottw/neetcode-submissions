class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurence_set = set()
        for num in nums:
            if num in occurence_set:
                return True
            else:
                occurence_set.add(num)
        return False