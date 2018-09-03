import time
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left_ = 0
        right_ = len(height) - 1
        while(left_ < right_):
            area = max(area, (right_ - left_) * min(height[right_], height[left_]))
            if height[left_] < height[right_]:
                left_ += 1
            else:
                right_ -= 1
        return area

    def __init__(self, height):
        self.height = height

    def getans(self, height):
        print(Solution.maxArea(self, height))

def main():
    list_ = [1,8,6,2,5,4,8,3,7]
    start = time.clock()
    a = Solution(list_)
    a.getans(list_)
    end = time.clock()
    print('Runing time:%s Seconds' % (end - start))


if __name__ == '__main__':
    main()