class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for curr in asteroids:
            alive = True
            
            while alive and curr < 0 and stack and stack[-1] > 0:
                if stack[-1] < abs(curr):    
                    stack.pop()
                elif stack[-1] == abs(curr):  
                    stack.pop()
                    alive = False
                else:                           
                    alive = False
            
            if alive:
                stack.append(curr)
        
        return stack