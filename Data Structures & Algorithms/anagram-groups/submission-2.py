class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {} # use hashtable to store like strs and their grouped characters

        for ch in strs:
            sorted_ch = "".join(sorted(ch))
            if sorted_ch not in seen:
                seen[sorted_ch] = []

            seen[sorted_ch].append(ch)
        return list(seen.values())

        