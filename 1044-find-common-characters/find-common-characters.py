class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = {}

        for ch in words[0]:
            freq[ch] = freq.get(ch, 0) + 1
        
        for word in words[1:]:
            current = {}

            # get the count of the current word for comparsion
            for ch in word:
                current[ch] = current.get(ch, 0) + 1

            # know how many duplicate or the character is by taking the minimum
            for ch in freq:
                freq[ch] = min(freq[ch],current.get(ch, 0))
                
        result = []
        # append the character by number of common occurance 
        for ch, count in freq.items():
            result += [ch] * count
        
        return result