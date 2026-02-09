class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # calcualte the ditance of mine using ditance formula x1 - x2 + y1 -y2 for grid up,down,left,right since we startat 0 ignoree them and add the targets
        my_distance = abs(target[0]) + abs(target[1])

        for x, y in ghosts:
            # calculate tyhe ghost movement to that os the target
            ghost_distance  = abs(target[0] - x) + abs(target[1] - y)
            # if the ghost reach brfore me or equal to me i can't escape 
            if ghost_distance <= my_distance:
                return False
        return True

