class Solution:
    def countBits(self, n: int) -> List[int]:
        bit_num_array = []
        for i in range(n + 1):
            if i == 0:
                bit_num_array.append(0)
                continue
            rem = i % 2
            curr_sum = bit_num_array[i // 2] + rem
            bit_num_array.append(curr_sum)
        return bit_num_array


class BruteForceSolution:
    def countBits(self, n: int) -> List[int]:
        bit_array = []
        for i in range(n + 1):
            bit_array.append(self.binaryOneNums(i))
        return bit_array

    def binaryOneNums(self, n: int) -> int:
        ans = 0
        while n > 0:
            rem = n % 2
            ans = ans + rem
            n = n // 2
        return ans
