class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        for i in s:
            if i in par:
                stack.append(i)
            elif len(stack) == 0 or par[stack.pop()] != i:
                return False
        return len(stack) == 0