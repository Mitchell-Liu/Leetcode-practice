class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        lside = 0
        rside = len(height)-1
        if len(height) > 100000 or len(height) < 2:
            return 0
        while lside != rside:
            max_area = (max(max_area,((rside-lside)*min(height[lside],height[rside]))))
            if height[lside] < height [rside]:
                lside += 1
            else:
                rside -= 1
        return max_area