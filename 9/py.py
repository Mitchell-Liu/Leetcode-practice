class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        rev_str = ''
        for i in range(len(x)-1,-1,-1):
            rev_str += x[i]
        if rev_str == x:
            return True
        else:
            return False