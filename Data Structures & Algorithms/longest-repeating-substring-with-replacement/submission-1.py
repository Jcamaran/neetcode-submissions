class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        res = l = maxf = 0

        for r in range(len(s)):
            # add the count to the current chracter bring added
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(maxf,count[s[r]])

            while (r - l + 1) - maxf > k: # while the current siz  of the window minus the count of character is greater than changes possible
                count[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res

        