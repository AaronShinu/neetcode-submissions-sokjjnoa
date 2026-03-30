class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute Force
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Optimal -> Hashset
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False