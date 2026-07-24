class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_t = {}
        t_s = {}

        for char_s, char_t in zip(s,t):
            if char_s in s_t and s_t[char_s] != char_t:
                return False
            if char_t in t_s and t_s[char_t] != char_s:
                return False

            s_t[char_s] = char_t
            t_s[char_t] = char_s

        return True

        
        