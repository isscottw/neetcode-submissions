class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcddcbabcd

        # last_seen map
        # for each: add to map with last seen index
        # if s[r] already exist in map and index >= l:
        # update l to seen + 1, clear map, add update exist map
        #

        last_seen = {}
        max_len = 0
        l, r = 0, 0
        while r < len(s):
            if last_seen.get(s[r], -1) >= l:
                l = last_seen[s[r]] + 1
                last_seen[s[r]] = r
                r += 1
            else:
                max_len = max(max_len, r - l + 1)
                last_seen[s[r]] = r
                r += 1

        return max_len
