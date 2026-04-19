class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            bucket[cnt].append(num)

        result = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
