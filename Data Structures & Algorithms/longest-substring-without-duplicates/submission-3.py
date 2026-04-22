class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n) Space: O(n)
        last_seen = {}
        max_len, l = 0, 0
        for r in range(len(s)):
            if s[r] in last_seen:
                l = max(last_seen[s[r]] + 1, l)
            max_len = max(max_len, r - l + 1)
            last_seen[s[r]] = r
        return max_len