class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        current = ""
        k = 0

        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)

            elif ch == "[":
                count_stack.append(k)
                string_stack.append(current)
                current = ""
                k = 0

            elif ch == "]":
                repeat = count_stack.pop()
                prev = string_stack.pop()
                current = prev + repeat * current

            else:
                current += ch

        return current