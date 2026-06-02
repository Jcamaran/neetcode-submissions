class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        # Find all unique characters in the string to check each one individually
        charSet = set(s)

        # Iterate through each unique character, treating it as the target frequent character
        for c in charSet:
            count = l = 0
            
            # Use a sliding window to scan the entire string
            for r in range(len(s)):
                # If the character at the right pointer matches our target, increment its count
                if s[r] == c:
                    count += 1
                
                # Formula: (window length) - (count of target char) = number of replacements needed.
                # While the replacements needed exceed 'k', shrink the window from the left.
                while (r - l + 1) - count > k:
                    # If the character leaving the window matches our target, decrement its count
                    if s[l] == c: 
                        count -= 1
                    l += 1  # Move the left pointer forward

                # Update the maximum length of a valid window found so far
                res = max(res, r - l + 1)
            
        return res