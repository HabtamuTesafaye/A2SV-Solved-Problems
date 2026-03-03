class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        result = []

        while freq:
            max_char = None
            max_count = 0

            for ch in freq:
                if freq[ch] > max_count:
                    max_count = freq[ch]
                    max_char = ch

            for _ in range(max_count):
                result.append(max_char)

            del freq[max_char]

        return "".join(result)