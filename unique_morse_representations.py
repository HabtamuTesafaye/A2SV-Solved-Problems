class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."
        ]
        
        transform = set()
        
        for word in words:
            code = ""
            for ch in word:
                code += morse[ord(ch) - ord('a')]
            transform.add(code)
        
        return len(transform)
