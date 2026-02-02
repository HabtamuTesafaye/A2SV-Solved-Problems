class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        count = 0
        first_ch = second_ch = ""
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if count  == 0:
                    count += 1
                    first_ch = s1[i]
                    second_ch = s2[i]
                elif count == 1:
                    if not(s1[i] == second_ch and s2[i] == first_ch):
                        return False
                    count += 1
                else:
                    return False
        return True if count == 2 else False
