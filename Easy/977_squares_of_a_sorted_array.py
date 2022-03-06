class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = []
        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            n1 = nums[p1] ** 2
            n2 = nums[p2] ** 2

            if n1 > n2:
                new_list.append(n1)
                p1 += 1
            else:
                new_list.append(n2)
                p2 -= 1

        new_list.reverse()

        return new_list
