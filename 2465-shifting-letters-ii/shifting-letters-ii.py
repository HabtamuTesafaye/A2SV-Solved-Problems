class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
             # go forward
            if direction == 1: 
                diff[start] += 1
                diff[end + 1] -= 1
            # go backward
            else: 
                diff[start] -= 1
                diff[end + 1] += 1

        # prefix sum to get net shifts
        net_shifts = [0] * n
        curr = 0
        for i in range(n):
            curr += diff[i]
            net_shifts[i] = curr

        # apply shifts
        result = []
        for i, c in enumerate(s):
            new_pos = (ord(c) - ord('a') + net_shifts[i]) % 26
            result.append(chr(new_pos + ord('a')))

        return "".join(result)
