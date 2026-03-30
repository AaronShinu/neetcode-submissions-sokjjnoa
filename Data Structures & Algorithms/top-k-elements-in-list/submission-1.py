class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqArray = [[] for i in range(len(nums) + 1 )]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for num,val in count.items():
            freqArray[val].append(num)
        
        result = []
        for i in range(len(freqArray) - 1,0,-1):
            for n in freqArray[i]:
                result.append(n)
                if len(result) == k:
                    return result