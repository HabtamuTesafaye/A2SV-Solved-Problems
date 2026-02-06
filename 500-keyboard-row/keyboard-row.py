class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []
        
        for word in words:
            w = word.lower()
            
            if w[0] in row1:
                row = row1
            elif w[0] in row2:
                row = row2
            else:
                row = row3
            
            valid = True
            for ch in w:
                if ch not in row:
                    valid = False
                    break
            
            if valid:
                result.append(word)
        
        return result