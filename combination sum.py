__author__ = 'yuyue'

class Solution(object):
    def combinationSum(self, candidates, target):
        tempresult = []
        result = []
        flag=[0]
        candidates = sorted(candidates)
        length = len(candidates)

        def dfs(pos, candidates, length, target, result, tempresult,flag):
            tempresult.append(candidates[pos])
            if candidates[pos] == target:
                result.append(tempresult[:])
                tempresult.pop()
                return
            elif candidates[pos] > target:
                tempresult.pop()
                flag[0] = 1
                return
            else:
                for i in range(pos, length):
                    dfs(i, candidates, length, target - candidates[pos], result, tempresult,flag)
                    if flag[0]:
                        flag[0] = 0
                        break
                tempresult.pop()
                return


        for i in range(length):
            dfs(i,candidates,length,target,result,tempresult,flag)
        return result