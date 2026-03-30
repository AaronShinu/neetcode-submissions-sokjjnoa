class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        freq = [[] for i in range(len(nums) + 1 )]

        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0)
        for n,c in countMap.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result