class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        # we ininstialze a set to keep track of dupes

        charSet = set(s)


        for char in charSet:
            count = l = 0


            for r in range(len(s)):
                if s[r] == char:
                    count += 1
                

                while (r - l + 1) - count > k: # while the length of the winow -  the current freq of the char is greater than the amount of possible replacements
                    if s[l] == char:
                        count -= 1
                    l += 1
                
                res = max(res, r - l + 1)
        return res




        