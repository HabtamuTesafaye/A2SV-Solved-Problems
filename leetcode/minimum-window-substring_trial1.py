class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        needed_count = len(freq)

        # the current window varibales to track if we have all the chacrcter we need 
        matchs = 0
        window_count = {}
        left, right = 0, 0

        # best window found 
        min_len = float('inf')
        best_left = 0
        best_right = 0

        while right < len(s):
            current_char = s[right]
            window_count[current_char] = window_count.get(current_char, 0) + 1

            # check if the current char has the same coount on the current window 
            if current_char in freq and window_count[current_char] == freq[current_char]:
                matchs += 1

            # shrink the window for the smaller size
            while left <= right and needed_count == matchs:
                current_window_size = right - left + 1
                if current_window_size <  min_len:
                    min_len = current_window_size
                    best_left = left
                    best_right = right

                removed_char = s[left]
                window_count[removed_char]  -= 1

                # if the charcter breaks the requirment decrement matchs 
                if removed_char in freq and window_count[removed_char] < freq[removed_char]:
                    matchs -= 1

                left += 1

            right += 1
        
        if min_len == float("inf"):
            return ""
        else:
            return s[best_left: best_right + 1]
