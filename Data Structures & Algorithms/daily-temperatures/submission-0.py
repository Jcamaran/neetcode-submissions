class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        res = [0] * n

        stack = []

        for i,t in enumerate(temperatures):
            # while a stack exist and the temp is greater than the top of the stack
            while stack and t > stack[-1][0]:

                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t,i])
        return res

            
        