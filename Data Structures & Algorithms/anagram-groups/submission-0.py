from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) # Mapping character count of each string to list of anagrams
        
        for s in strs:
            count = [0] * 26 # a...z
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashMap[tuple(count)].append(s)
        
        return list(hashMap.values())