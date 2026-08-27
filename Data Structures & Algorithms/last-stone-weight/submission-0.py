class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1: 
            # because we turn the numbers negative we use the fact that heaps pop the smallest number from an array to ensure we have the two "largest" numbers
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first-second)

        stones.append(0)

        return abs(stones[0])


        