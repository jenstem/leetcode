# Maximum Area of Longest Diagonal Rectangle #3000

# You are given a 2D 0-indexed integer array dimensions.

# For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length and dimensions[i][1] represents the width of the rectangle i.

# Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the maximum area.

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = mx = 0
        for l, w in dimensions:
            t = l**2 + w**2
            if mx < t:
                mx = t
                ans = l * w
            elif mx == t:
                ans = max(ans, l * w)
        return ans