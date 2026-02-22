class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        for point1 in points:
            # map the distance to keep track of the current point
            distance = {}
            for point2 in points:
                # calculate the distance 
                dx = point1[0] - point2[0]
                dy = point1[1] - point2[1]
                current_distance = dx**2 + dy**2
                distance[current_distance] = distance.get(current_distance, 0) + 1


            for count in distance.values():
                total += count * (count - 1)
        return total
