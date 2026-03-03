class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score , reverse=True)
        rank_score_map = {}

        for i in range(len(sorted_scores)):
            if i == 0:
                rank_score_map[sorted_scores[i]] = "Gold Medal"
            elif i == 1:
                rank_score_map[sorted_scores[i]] = "Silver Medal"
            elif i == 2:
                rank_score_map[sorted_scores[i]] = "Bronze Medal"
            else:
                rank_score_map[sorted_scores[i]] = str(i + 1)

        #  build the orgibnal order
        result = []
        for s in score:
            result.append(rank_score_map[s])
        
        return result