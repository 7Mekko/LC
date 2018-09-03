class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == []:
            return 0
        length = len(height)
        l = 0
        r = length - 1
        h = 0
        max_ = 0
        for i in range(length):
            if height[i] > max_:
                max_ = height[i]
                h = i
        tmp = height[l]
        ans = 0
        while l < h:
            if tmp < height[l]:
                tmp = height[l]
            else:
                ans += (tmp - height[l])
            l += 1
        tmp = height[r]
        while r > h:
            if tmp < height[r]:
                tmp = height[r]
            else:
                ans += (tmp - height[r])
            r -= 1
        return ans