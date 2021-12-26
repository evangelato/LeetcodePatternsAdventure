class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum_seq = nums[0]

        for i in range(1, len(nums)):
            if sum_seq + nums[i] < nums[i]:
                sum_seq = nums[i]
            else:
                sum_seq = sum_seq + nums[i]
            if sum_seq > max_sum:
                max_sum = sum_seq

        return max_sum
