from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        
        return res
    
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     res = []

    #     if target <= 0:
    #         return []

    #     for i in range(len(candidates)):
    #         candidate = candidates[i]
    #         new_target = target - candidate
    #         if new_target < 0:
    #             continue
    #         if new_target == 0:
    #             res.append([candidate])
    #             continue
    #         for subset in self.combinationSum(candidates[i:], new_target):
    #             res.append([candidate] + subset)

    #     return res

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum(candidates = [2,3,6,7], target = 7))
    print(s.combinationSum(candidates = [2,3,5], target = 8))