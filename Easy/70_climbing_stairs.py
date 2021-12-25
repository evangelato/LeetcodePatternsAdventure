class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        ways = [0] * (n + 1)

        ways[0] = 1
        ways[1] = 1

        for i in range(2, len(ways)):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[-1]
