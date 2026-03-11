class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length_p , length_s = len(p), len(s)
        if length_p > length_s:
            return []
        
        p_count = Counter(p)
        s_count = Counter(s[:length_p])
        result = []

        if p_count == s_count:
            result.append(0)

        for i in range(length_p, length_s):
            s_count[s[i]] += 1
            s_count[s[i - length_p]] -= 1

            if s_count[s[i - length_p]] == 0:
                del s_count[s[i - length_p]]

            if s_count == p_count:
                result.append(i - length_p + 1)
        
        return result
