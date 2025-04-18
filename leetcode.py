# Prime in Diagonal #2614

# You are given a 0-indexed two-dimensional integer array nums.

# Return the largest prime number that lies on at least one of the diagonals of nums. In case, no prime is present on any of the diagonals, return 0.

# Note that:

# An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.
# An integer val is on one of the diagonals of nums if there exists an integer i for which nums[i][i] = val or an i for which nums[i][nums.length - i - 1] = val.

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            return all(x % i for i in range(2, int(sqrt(x)) + 1))

        n = len(nums)
        ans = 0
        for i, row in enumerate(nums):
            if is_prime(row[i]):
                ans = max(ans, row[i])
            if is_prime(row[n - i - 1]):
                ans = max(ans, row[n - i - 1])
        return ans