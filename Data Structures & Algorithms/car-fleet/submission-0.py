class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]

        pair.sort(reverse = True)

        stack = [] # stores time it takes for car to get to target

        for p,s in pair:
            stack.append((target - p) /  s)
            if len(stack) >= 2 and stack [-1] <= stack[-2]: # if the currnet car will join a fleet before reaching target
                stack.pop()
        return len(stack)
        
        