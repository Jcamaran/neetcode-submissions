class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # The counter approach
        ans = []

        counterN = Counter(nums).most_common()

        for i in range(k):
            ans.append(counterN[i][0])
        return ans



        