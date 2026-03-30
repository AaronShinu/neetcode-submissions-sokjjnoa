from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) # Map char to ascii index values from a .. z 

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1 
            hashMap[tuple(count)].append(word)
        
        return list(hashMap.values())