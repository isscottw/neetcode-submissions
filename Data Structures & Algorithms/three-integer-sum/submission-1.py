class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        # [-1,0,1,2,-1,-4]
        # [-4,-1,-1,0,1,2]

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur_three_sum = nums[i] + nums[l] + nums[r]
                if l < r and cur_three_sum < 0:
                    l += 1
                elif l < r and cur_three_sum > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return result