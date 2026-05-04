class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, target):
            # If the target is met, add the current combination to the results
            if target == 0:
                result.append(path)
                return
            # If the target goes negative, stop the exploration
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                # Include the candidate and continue the search
                backtrack(i, path + [candidates[i]], target - candidates[i])
        
        result = []
        backtrack(0, [], target)
        return result