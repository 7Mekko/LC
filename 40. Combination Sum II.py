class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def _combinationSum2(candidates, target, ans, tmp, i):
            if target == 0:
                try:
                    ans.index(tmp)
                except:
                    ans.append(tmp[:])

            else:
                for j in range(i, len(candidates)):
                    if j > 0 and candidates[j] == candidates[j - 1] and len(tmp) == 0:
                        continue
                    num = candidates[j]
                    if num > target:
                        return
                    tmp.append(num)
                    target -= num
                    _combinationSum2(candidates, target, ans, tmp, j + 1)
                    if len(tmp) > 0:
                        tmp.pop()
                    target += num

        ans = []
        tmp = []
        candidates.sort()
        i = 0
        _combinationSum2(candidates, target, ans, tmp, i)
        return ans