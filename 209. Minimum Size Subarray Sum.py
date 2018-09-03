class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = l = 0
        n = len(nums)
        if n < 1:
            return 0
        r = n - 1
        sum = nums[0]
        if sum >= s:
            return 1
        for j in range(1,n):
            if sum < s:
                sum += nums[j]
            if sum >= s and j - i <= r - l:
                l, r = i, j
            while i < j and sum >= s:
                if j - i <= r - l:
                    l, r = i, j
                if j == n - 1 and sum - nums[i] < s:
                    break
                sum -= nums[i]
                i += 1
            if sum >= s and j - i <= r - l:
                l, r = i, j
        if sum < s and j - i == n - 1:
            return 0
        print("sum=",sum,"c=",nums[j],"i=",i,"j=",j,"l=",l,"r=",r)
        return r - l + 1