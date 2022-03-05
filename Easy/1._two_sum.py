class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, v in enumerate(nums):
            if (target - v) in seen:
                return [seen[target - v], i]
            else:
                seen[v] = i
        return []


class TwoPointerSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 0:
            return []

        index_nums = []
        for i, v in enumerate(nums):
            index_nums.append((v, i))

        sorted_index_nums = self.mergeSort(index_nums)
        p1 = 0
        p2 = len(sorted_index_nums) - 1

        while p1 < p2:
            if sorted_index_nums[p1][0] + sorted_index_nums[p2][0] == target:
                return [sorted_index_nums[p1][1], sorted_index_nums[p2][1]]
            if sorted_index_nums[p1][0] + sorted_index_nums[p2][0] < target:
                p1 += 1
            if sorted_index_nums[p1][0] + sorted_index_nums[p2][0] > target:
                p2 -= 1

    def mergeSort(self, list: List) -> List:
        if len(list) <= 1:
            return list
        mid = len(list) // 2
        left = self.mergeSort(list[:mid])
        right = self.mergeSort(list[mid:])
        return self.mergeLists(left, right)

    def mergeLists(self, list1: List, list2: List) -> List:
        result = []
        i1 = 0
        i2 = 0
        while i1 < len(list1) and i2 < len(list2):
            if list1[i1][0] < list2[i2][0]:
                result.append(list1[i1])
                i1 += 1
            else:
                result.append(list2[i2])
                i2 += 1

        if i1 < len(list1):
            result = result + list1[i1:]
        if i2 < len(list2):
            result = result + list2[i2:]

        return result
