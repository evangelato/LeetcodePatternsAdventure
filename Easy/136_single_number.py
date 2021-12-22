class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}

        for i in nums:
            if i not in hash_table:
                hash_table[i] = 1
            else:
                hash_table.pop(i)

        return list(hash_table.keys())[0]
