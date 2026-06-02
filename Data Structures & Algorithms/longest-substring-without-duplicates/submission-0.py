class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()

        lng = 0

        left = 0
        for right in range(len(s)):
            # we want to check wether its an invalid window
            while s[right] in window:
                window.remove(s[left])
                left += 1
            lng = max(lng, right -left +1)
            window.add(s[right])
        return lng
            
        