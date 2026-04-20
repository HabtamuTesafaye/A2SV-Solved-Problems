class Solution:
    def decodeString(self, s: str) -> str:
        stack = []     
        current = ""
        k = 0

        for char in s:
            if char.isdigit():
                # handles multi-digit like 12[...]
                k = k * 10 + int(char) 
            elif char == '[':
                stack.append((current, k)) 
                current = ""
                k = 0
            elif char == ']':
                prev_str, repeat = stack.pop()
                current = prev_str + current * repeat
            else:
                current += char          

        return current