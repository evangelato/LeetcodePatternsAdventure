class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_table = {}
        for i in nums:
            hash_table[i] = True
        for i in range(len(nums)):
            if i not in hash_table:
                return i
        return len(nums)
