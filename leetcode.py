# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        ways = [0] * (n + 1)
        ways[0], ways[1] = 1, 1
        for i in range(2, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        return ways[n]