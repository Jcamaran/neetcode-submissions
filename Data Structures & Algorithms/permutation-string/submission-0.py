class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # First, check whether the length of s1 is greater than s2.
        # If it is, return False.
        if len(s1) > len(s2):
            return False

        # Initialize two hash maps to compare character counts.
        s1_count = {}
        s2_count = {}

        # Iterate through s1 and create hash maps for both strings.
        # If they are equal, immediately return True.
        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
            s2_count[s2[i]] = 1 + s2_count.get(s2[i], 0)

        if s1_count == s2_count:
            return True

        # Initialize the left pointer.
        left = 0

        # Iterate starting at the index after the length of s1
        # to the end of s2 using a sliding window.
        for right in range(len(s1), len(s2)):
            # Add the right character to the current window while removing
            # the left character so we keep a window size of len(s1).
            s2_count[s2[right]] = 1 + s2_count.get(s2[right], 0)
            s2_count[s2[left]] -= 1

            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]

            left += 1

            if s1_count == s2_count:
                return True

        return False