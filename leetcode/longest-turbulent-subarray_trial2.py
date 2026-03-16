class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)
    
        max_length = 1
        current_length = 1
        
        for i in range(1, len(arr)):
            # Determine the comparison between current and previous element
            if arr[i] == arr[i - 1]:
                current_length = 1
            elif i == 1:
                # Start with length 2 if first two elements are different
                current_length = 2
            else:
                # Check if the comparison sign flipped
                if (arr[i] > arr[i - 1]) != (arr[i - 1] > arr[i - 2]):
                    current_length += 1
                else:
                    # Sign didn't flip - start new window
                    current_length = 2
            
            max_length = max(max_length, current_length)
        
        return max_length