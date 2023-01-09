class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) == 0:
             return -1
        elif len(needle)>len(haystack):
            return -1
        x = haystack.find(needle)
        return x