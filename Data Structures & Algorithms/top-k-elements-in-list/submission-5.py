class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums).most_common()
        ans = []

        for i in range(k):
            ans.append(c[i][0])

        return ans



        