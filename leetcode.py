# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0

        for i, char in enumerate(reversed(columnTitle)):
            result += (ord(char) - ord('A') + 1) * (26 ** i)
        return result