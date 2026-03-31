class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        freqArray = [[] for i in range(len(nums) + 1)]

        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0)
        for num, value in countMap.items():
            freqArray[value].append(num)

        k_result = []
        for i in range(len(freqArray) - 1, 0, -1):
            for n in freqArray[i]:
                k_result.append(n)
                if len(k_result) == k:
                    return k_result