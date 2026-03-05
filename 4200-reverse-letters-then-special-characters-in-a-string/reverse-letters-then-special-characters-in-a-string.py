class Solution:
    def reverseByType(self, s: str) -> str:
        letter = []
        specail_char  = []

        # map the lettter and character for mapping
        for char in s:
            if char.isalpha():
                letter.append(char)
            else:
                specail_char.append(char)

        letter.reverse()
        specail_char.reverse()

        # build the result based on the position of the char type
        i = j = 0
        result = []
        for char in s:
            if char.isalpha():
                result.append(letter[i])
                i += 1
            else:
                result.append(specail_char[j])
                j += 1

        return "".join(result)