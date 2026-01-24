class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            # If opening bracket → push
            if char in mapping.values():
                stack.append(char)

            # If closing bracket
            elif char in mapping:
                # No opening bracket OR wrong match
                if not stack or stack.pop() != mapping[char]:
                    return False

        # Valid only if no unclosed brackets remain
        return len(stack) == 0
