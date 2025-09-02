class Solution:
    #ayush
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for  a in s:
            index = ord(a) - ord('a')
            count[index] +=1
        for b in t:
            index = ord(b) - ord('a')
            count[index] -=1
        for c in count:
            if c !=0:
                return False
        return True