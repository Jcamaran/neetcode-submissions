class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []


        for i,t in enumerate(temperatures):
            # while stack and the temp is higher than the top of the stack
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop() # we get the last stacked temp and index

                res[stackInd] = i - stackInd # the result indexs day would be the curr index - the last time we saw a higher temp
            stack.append([t,i])
        return res

        