class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        long_pref = ''
        index = 0
        strs.sort()
        print(strs)

        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                long_pref += strs[0][i]
            else:
                break

        return long_pref