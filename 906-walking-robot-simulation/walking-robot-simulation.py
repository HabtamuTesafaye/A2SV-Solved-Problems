class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0  
        direction_index = 0 
        obstacles_set = set(map(tuple, obstacles))  
        max_distance_squared = 0

        for command in commands:
            if command == -2:  # Turn left
                direction_index = (direction_index - 1) % 4
            elif command == -1:  # Turn right
                direction_index = (direction_index + 1) % 4
            else:  # Move forward
                for _ in range(command):
                    # Calculate the next position
                    next_x = x + directions[direction_index][0]
                    next_y = y + directions[direction_index][1]
                    if (next_x, next_y) not in obstacles_set:  # Check for obstacles
                        x, y = next_x, next_y  # Move to the next position
                        # Calculate the squared distance from the origin
                        max_distance_squared = max(max_distance_squared, x * x + y * y)

        return max_distance_squared