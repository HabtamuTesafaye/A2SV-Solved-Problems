class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        doubled = s + s
        n = len(s)
        
        for i in range(len(doubled) - n + 1):
            if doubled[i : i + n] == goal:
                return True
                
        return False