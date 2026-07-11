class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens:
            if n == "+":
                x,y = stack.pop(), stack.pop()
                stack.append(x + y)
            elif n == "-":
                x,y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif n == "*":
                x,y = stack.pop(), stack.pop()
                stack.append(x * y)
            elif n == "/":
                x,y = stack.pop(), stack.pop()
                stack.append(int(float(y) / x))
            else:
                stack.append(int(n))
        return stack[0]

 




        