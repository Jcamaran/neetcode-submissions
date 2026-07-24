class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # immedietly i think of a set to not include repearing characters
        # a sliding window to find said substring

        setS = set()

        l = res = 0

        for r in range(len(s)):
            while s[r] in setS:
                setS.remove(s[l])
                l += 1
            
            
            res = max(res, r-l+1)
            setS.add(s[r])


          
        return res

        