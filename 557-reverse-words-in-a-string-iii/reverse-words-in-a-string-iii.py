class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reversed_word = [word[::-1] for word in words]
        return " ".join(reversed_word)