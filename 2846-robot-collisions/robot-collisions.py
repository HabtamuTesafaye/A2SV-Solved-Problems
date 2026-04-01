class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
    
        # Create list of (position, health, direction, original_index)
        robots = [(positions[i], healths[i], directions[i], i) for i in range(n)]
        
        # Sort by position
        robots.sort()
        
        stack = []  # Stack of R robots: (health, original_index)
        survivors = {}  # original_index -> final_health
        
        for pos, health, direction, orig_idx in robots:
            if direction == 'R':
                # R robot goes on stack, waiting for potential collision
                stack.append([health, orig_idx])
            else:  # direction == 'L'
                # L robot collides with R robots in stack
                current_health = health
                
                while stack and current_health > 0:
                    r_health, r_idx = stack[-1]
                    
                    if r_health > current_health:
                        # R robot wins, L robot dies
                        stack[-1][0] -= 1  # Decrease R robot's health
                        current_health = 0
                    elif r_health < current_health:
                        # L robot wins, R robot dies
                        stack.pop()
                        current_health -= 1
                    else:  # r_health == current_health
                        # Both die
                        stack.pop()
                        current_health = 0
                
                # If L robot survived all collisions
                if current_health > 0:
                    survivors[orig_idx] = current_health
        
        # Add surviving R robots from stack
        for health, orig_idx in stack:
            survivors[orig_idx] = health
        
        # Return in original order
        result = []
        for i in range(n):
            if i in survivors:
                result.append(survivors[i])
        
        return result