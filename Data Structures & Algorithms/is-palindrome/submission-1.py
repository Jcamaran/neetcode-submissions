class Solution:
    def isPalindrome(self, s: str) -> bool:
        joined_s = "".join(char.lower() for char in s if char.isalnum())

        reversed_s = joined_s[::-1]




        return reversed_s == joined_s
