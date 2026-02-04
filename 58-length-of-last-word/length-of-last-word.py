class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()

        # Split by spaces
        words = s.split()

        return len(words[-1])