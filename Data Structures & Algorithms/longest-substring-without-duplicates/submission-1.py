class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # here we could use a set which checks wether the curr character has been seen if so we move the window

        set_s = set()


        l = res = 0

        for r in range(len(s)):
            while s[r] in set_s: # we use a while loop because we want to iterate until the current right char is no linger in the string (no duplicates)
                set_s.remove(s[l])
                l += 1
            set_s.add(s[r])

            res = max(res,r - l + 1)
        return res



    