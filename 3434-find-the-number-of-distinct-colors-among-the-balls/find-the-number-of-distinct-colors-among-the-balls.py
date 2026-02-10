class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_map = {}
        color_count = {}
        result = []

        for ball, color in queries:
            if ball in ball_map:
                color_before = ball_map[ball]
                color_count[color_before] -= 1
                if color_count[color_before] == 0:
                    del color_count[color_before]

            ball_map[ball] = color
            color_count[color] =color_count.get(color, 0) + 1
            
            result.append(len(color_count)) 
        return result
            