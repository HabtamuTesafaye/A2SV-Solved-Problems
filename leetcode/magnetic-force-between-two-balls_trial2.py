class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
    
        def can_place_balls(min_dist):
            count = 1
            last_pos = position[0]
            for pos in position[1:]:
                if pos - last_pos >= min_dist:
                    count += 1
                    last_pos = pos
                    if count == m:
                        return True
            return False

        left, right = 1, position[-1] - position[0]
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if can_place_balls(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer