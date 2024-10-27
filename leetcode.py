# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        title = ""

        while columnNumber > 0:
            columnNumber -= 1
            title = chr(columnNumber % 26 + ord('A')) + title
            columnNumber //= 26
        return title