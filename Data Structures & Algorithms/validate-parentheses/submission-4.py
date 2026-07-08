class Solution:
    def isValid(self, s: str) -> bool:
        valid = { "(" : ")", "[" : "]", "{" : "}" }


        stack = [] # we will use a stack to keep track of matching brackets


        for char in s:
            if char in valid: # open bracket
                stack.append(char)
            else: # closing bracket
                if not stack or valid[stack.pop()] != char: # if the most recently popped open bracket is not equal to the curr closing char its not valid
                    return False
        return not stack

