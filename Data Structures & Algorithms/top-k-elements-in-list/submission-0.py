class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time: O(nlogk) Space: O(n + k)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        h = []
        for num, c in count.items():
            heapq.heappush(h, (c, num))
            if len(h) > k:
                heapq.heappop(h)
        
        result = []
        while (len(h) > 0):
            result.append(heapq.heappop(h)[1])
        return result
