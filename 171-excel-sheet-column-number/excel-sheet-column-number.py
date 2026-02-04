class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        power = 1

        for ch in reversed(columnTitle):
            result += (ord(ch) - ord('A') + 1) * power
            power *= 26

        return result