class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        og_num_str = str(x)
        rev_num = 0
        
        if x<0:
            for i in range(len(og_num_str)-1):
                rev_num -= int(og_num_str[i+1])*(10**i)
        else:
            for i in range(len(og_num_str)):
                rev_num += int(og_num_str[i])*(10**i)
        if rev_num > 2147483647 or rev_num < -2147483648:
            return 0
        return rev_num