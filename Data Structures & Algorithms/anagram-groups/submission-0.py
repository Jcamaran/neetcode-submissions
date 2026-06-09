class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}



        for char in strs:
            sorted_w = "".join(sorted(char))


            if sorted_w not in seen:
                seen[sorted_w] = []
            
            seen[sorted_w].append(char)
        
        return list(seen.values())





        