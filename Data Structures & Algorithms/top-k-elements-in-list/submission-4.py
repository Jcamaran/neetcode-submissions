
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # here we canm use the most_common() method which orders the hashtable created by the Counter class

        counted_n = Counter(nums).most_common()
        ans = []


        for i in range(k):
            ans.append(counted_n[i][0])

        return ans


        