class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = self.searchRecursive(nums, target, 0, len(nums) - 1)

        return result

    def searchRecursive(
        self, nums: List[int], target: int, left_index: int, right_index: int
    ):
        if left_index > right_index:
            return -1

        mid_index = (left_index + right_index) // 2

        if nums[mid_index] == target:
            return mid_index
        elif target < nums[mid_index]:
            return self.searchRecursive(nums, target, left_index, mid_index - 1)
        else:
            return self.searchRecursive(nums, target, mid_index + 1, right_index)
