class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0, len(numbers)-1


        while left < right:
            bsum = numbers[right] + numbers[left]

            if bsum == target:
                return [left + 1, right +1]
            
            if bsum < target:
                left +=1 
            if bsum > target :
                right -= 1
           
        return []
