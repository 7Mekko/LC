class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def _combinationSum(candidates,target,ans,tmp,i):
            if target == 0:
                ans.append(tmp[:])
                return
            else:
                for j in range(i,len(candidates)):
                    num = candidates[j]
                    if num > target:
                        return
                    tmp.append(num)
                    target -= num
                    _combinationSum(candidates,target,ans,tmp,j)
                    if len(tmp) > 0:
                        tmp.pop()
                    target += num
        ans = []
        tmp = []
        candidates.sort()
        i = 0
        _combinationSum(candidates,target,ans,tmp,i)
        return ans