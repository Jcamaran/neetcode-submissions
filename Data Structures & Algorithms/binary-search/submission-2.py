class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search works only with a non deacreasing array / sorted

        # works in O(log n) time because it cuts the array in half every single time.

        l,r = 0,len(nums) -1

        while l <= r: # must be less than or eqail to in case there is only one element
            mid = (r + l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target: 
                l = mid + 1
            else:
                r = mid - 1
        return -1
        