class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        second = 0
        m = len(t)
        for first in range(len(s)):
            if second < m and  s[first] == t[second]:
                second += 1

        return m - second