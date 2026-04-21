class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time: O(n) Space: O(1)
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not self.isAlphanumeric(s[start]):
                start += 1
            while start < end and not self.isAlphanumeric(s[end]):
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

    def isAlphanumeric(self, c):
        # built-in: string.isalnum()
        return (
            ord("a") <= ord(c) <= ord("z")
            or ord("A") <= ord(c) <= ord("Z")
            or ord("0") <= ord(c) <= ord("9")
        )
