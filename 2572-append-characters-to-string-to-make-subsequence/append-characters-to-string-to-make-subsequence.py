class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # first , second = 0, 0
        # n , m = len(s), len(t)

        # while first < n and second < m:
        #     # find the common char and increment to get the chars to add to s from t 
        #     if s[first] == t[second]:
        #         second += 1

        #     first += 1

        # return m - second

        second = 0
        m = len(t)
        for first in range(len(s)):
            if second < m and  s[first] == t[second]:
                second += 1

        return m - second


