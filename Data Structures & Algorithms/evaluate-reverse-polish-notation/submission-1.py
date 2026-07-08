class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ans = 0

        for char in tokens:
            if char ==  "+":
                first,sec = stack.pop(), stack.pop()
                stack.append(first + sec)
            elif char == "-":
                first,sec = stack.pop(), stack.pop()
                stack.append(sec - first)
                
            elif char == "*":
                first,sec = stack.pop(), stack.pop()
                stack.append(first * sec)

            elif char == "/":
                first,sec = stack.pop(), stack.pop()
                stack.append(int(float(sec) / first))
            else:
                stack.append(int(char))

        return stack[0]


        