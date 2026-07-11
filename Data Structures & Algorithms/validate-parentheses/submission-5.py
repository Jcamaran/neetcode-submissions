class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            "{":"}",
            "(":")",
            "[":"]",
        }
        stack = []

        for char in s: 
            if char not in valid: # closing characters
                if not stack or valid[stack.pop()] != char:
                    return False
            else:  # opening brackets
                stack.append(char)
        return not stack
        

        
        