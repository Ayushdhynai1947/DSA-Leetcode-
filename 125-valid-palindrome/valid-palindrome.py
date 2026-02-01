class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = []
        
        for ch in s:
            if ch.isalnum():
                cleaned.append(ch.lower())
        
        cleaned_str = "".join(cleaned)
        return cleaned_str == cleaned_str[::-1]
