class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit_mask = 0

        for i in nums:
            bit_mask = bit_mask ^ i

        return bit_mask
