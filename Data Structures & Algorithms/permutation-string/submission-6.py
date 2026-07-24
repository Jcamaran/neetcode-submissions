class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = {}
        s2_count = {}

        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i],0)
            s2_count[s2[i]] = 1 + s2_count.get(s2[i],0)

        if s1_count == s2_count:
            return True # this is best case scenario the first len(s1) contain a permutation

        
        #otherwise we must use a sliding window to iterate from the end of s1 

        l = 0

        for r in range(len(s1), len(s2)):
            # WE MUST add a new char to the s2 window

            s2_count[s2[r]] = 1 + s2_count.get(s2[r],0)
            s2_count[s2[l]] -= 1

            if s2_count[s2[l]] == 0:
                del s2_count[s2[l]]
            
            l += 1

            if s1_count == s2_count: 
                return True
        return False

        