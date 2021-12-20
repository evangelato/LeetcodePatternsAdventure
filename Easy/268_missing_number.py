class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums = self.mergeSort(nums)
        for index, val in enumerate(sorted_nums):
            if index != val:
                return index
        return len(nums)

    def mergeSort(self, arr):
        if len(arr) > 1:
            return_arr = [0] * len(arr)
            mid = len(arr) // 2

            L = arr[:mid]
            R = arr[mid:]

            sorted_L = self.mergeSort(L)
            sorted_R = self.mergeSort(R)

            l_index = r_index = sorted_index = 0

            while l_index < len(sorted_L) and r_index < len(sorted_R):
                if sorted_L[l_index] < sorted_R[r_index]:
                    return_arr[sorted_index] = sorted_L[l_index]
                    l_index += 1
                else:
                    return_arr[sorted_index] = sorted_R[r_index]
                    r_index += 1
                sorted_index += 1

            while l_index < len(sorted_L):
                return_arr[sorted_index] = sorted_L[l_index]
                l_index += 1
                sorted_index += 1

            while r_index < len(sorted_R):
                return_arr[sorted_index] = sorted_R[r_index]
                r_index += 1
                sorted_index += 1
            return return_arr
        else:
            return arr
