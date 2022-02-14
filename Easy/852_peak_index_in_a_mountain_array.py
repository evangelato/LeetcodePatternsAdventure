class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        result = self.searchRecursive(arr, 0, len(arr) - 1)

        return result

    def searchRecursive(self, arr: List[int], left_index: int, right_index: int):

        mid_index = (left_index + right_index) // 2

        if arr[mid_index - 1] < arr[mid_index] and arr[mid_index] > arr[mid_index + 1]:
            return mid_index
        elif (
            arr[mid_index - 1] > arr[mid_index] and arr[mid_index] > arr[mid_index + 1]
        ):
            return self.searchRecursive(arr, left_index, mid_index - 1)
        else:
            return self.searchRecursive(arr, mid_index + 1, right_index)


class LinearSolution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i, e in enumerate(arr):
            if e > arr[i + 1]:
                return i
