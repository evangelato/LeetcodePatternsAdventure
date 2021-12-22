class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_table = {}
        for i in nums:
            hash_table[i] = True
        missing = []
        for i in range(1, len(nums) + 1):
            if i not in hash_table:
                missing.append(i)
        return missing
